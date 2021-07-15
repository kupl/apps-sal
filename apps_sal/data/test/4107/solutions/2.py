import sys
input = sys.stdin.readline

n,k=list(map(int,input().split()))
s=input().strip()


seg_el=1<<((n+k+1).bit_length())# Segment treeの台の要素数
SEG=[1<<40]*(2*seg_el)# 1-indexedなので、要素数2*seg_el.Segment treeの初期値で初期化

def getvalue(n,seg_el):
    i=n+seg_el
    ANS=1<<40
    
    ANS=min(SEG[i],ANS)
    i>>=1# 子ノードへ
    
    while i!=0:
        ANS=min(SEG[i],ANS)
        i>>=1

    return ANS

def updates(l,r,x):# 区間[l,r)に関するminを調べる
    L=l+seg_el
    R=r+seg_el

    while L<R:
        if L & 1:
            SEG[L]=min(x,SEG[L])
            L+=1

        if R & 1:
            R-=1
            SEG[R]=min(x,SEG[R])
        L>>=1
        R>>=1

updates(n,n+k+1,0)

for i in range(n-1,-1,-1):
    if s[i]=="0":
        x=getvalue(i+1,seg_el)
        updates(i,i+1,x+i+1)
    else:
        x=getvalue(i+k+1,seg_el)
        updates(max(0,i-k),i+k+1,x+i+1)
    
print(getvalue(0,seg_el))


