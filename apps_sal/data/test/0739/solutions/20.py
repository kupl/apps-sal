import numpy as np
import sys

def II(): return int(sys.stdin.readline())
def MI(): return list(map(int, sys.stdin.readline().split()))
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

# だいたいpdfの通り
def main():
    l,a,b,md=MI()

    # 数列の要素がk桁になるのがi項目で、k+1桁になるのがj項目
    k=0
    i=0
    ans=[0,a%md,b%md]
    ans=np.array(ans,dtype="i8")
    # 各桁数ごとに処理
    while i<l:
        k+=1
        j=(10**k-a+b-1)//b
        if j<=0:continue
        if j>l:j=l
        # k桁の要素の個数がe
        e=j-i
        # i項目まで連結した整数をans[i],数列のi項目をs[i]とすると
        #                                       [10**k 0 0]
        # [ans[i],s[i],b] = [ans[i-1],s[i-1],b] [  1   1 0]
        #                                       [  0   1 1]
        # 最後の3x3行列をbbとして、e乗すればよいので、繰り返し二乗法でやる
        bb=np.zeros((3,3),dtype="i8")
        bb[0,0]=pow(10,k,md)
        bb[1,0]=bb[1,1]=bb[2,1]=bb[2,2]=1
        while e:
            if e&1:ans=np.dot(ans,bb)%md
            bb=np.dot(bb,bb)%md
            e>>=1
        i=j

    print((ans[0]))

main()

