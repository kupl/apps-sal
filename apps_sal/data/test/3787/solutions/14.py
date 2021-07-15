N, A, B = list(map(int, input().split()))
ans = []
 
if A+B-1<=N<=A*B:
    S = N-A
    cur = N
    ans = []
    for i in range(A+1):
        num = min(B-1, S)+1
        S -= num-1
        for j in range(num):
            ans.append(cur-num+1+j)
        cur -= num
    ans = ans[::-1][1:]
    print((*ans))
else:
    print((-1))

