N = int(input())
A = []
for _ in range(N):
    a = int(input())
    b = []
    for _ in range(a):
        b.append(list(map(int, input().split())))
    A.append(b)
# 証言リスト A[i人目][j個目の証言] -> [誰が, bit(1は正、0は誤)]

# bitが1であれば正しい証言、0であれば間違った証言とする
# 正しい証言だけ確認して、[i, 1]と証言した i も1かどうか、[j,0]と証言したjが0かどうか



def F(i):
    cnt = 0
    B = [-1]*N                #B = [-1,-1,-1]
    r = 0
    for j in range(N):    # i=1,  j=0,1,2
        if (i>>j)&1:         # 001 ->  1,0,0  j=0
            r += 1               # r = 1    
            if B[j] == 0:     #B[0] == -1  
                return 0
            B[j]=1              # B = [1,-1,-1]   
            for p,q in A[j]: # A[0] = [[2, 1], [3, 0]]   
                if q == 0:
                    if B[p-1]==1:  # B[2] == -1
                        return 0
                    B[p-1] = 0  # B = [1,1,0]
                else:
                    if B[p-1]==0:  # B[1] == -1
                        return 0
                    B[p-1] = 1      # B = [1,1,-1]
            else:
                cnt += 1          # cnt = 1
        else:         # j=1
            if B[j]==1:       #B[1] ==1
                return 0
            B[j]=0
            
    if cnt == r:
        return cnt

ans = 0
for i in range(1<<N):
    ans = max(ans,F(i))
print(ans)
