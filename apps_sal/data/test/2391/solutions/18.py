N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

A.append(A[0])
B.append(B[0])

AX=[]
BX=[]
for i in range(N):
    AX.append(A[i]^A[i+1])
    BX.append(B[i]^B[i+1])

AX+=AX[:-1]

# MP法


LEN=len(BX)
MP=[-1]*(LEN+1) #「接頭辞と接尾辞が最大何文字一致しているか」を記録する配列
NOW=-1 # 何文字一致しているか.

for i in range(LEN):
    while NOW>=0 and BX[i]!=BX[NOW]: # 一致していなかったら0から数え直すのではなく, MP[NOW]から数える.
        NOW=MP[NOW]
    NOW+=1
    MP[i+1]=NOW

LEN2=len(AX)

MP_SEARCH=[0]*(LEN2) # その文字までで何個一致しているかを調べる. LEN文字一致したらSが検出できたということ.
NOW=0
for i in range(LEN2):
    while NOW>=0 and AX[i]!=BX[NOW]:
        NOW=MP[NOW]
    NOW+=1
    MP_SEARCH[i]=NOW

    if NOW==LEN: # LEN文字一致したら, MP[LEN]から数える.
        NOW=MP[NOW]
        
for i in range(LEN2):
    if MP_SEARCH[i]==LEN:
        print(i-LEN+1,A[i-LEN+1]^B[0])
