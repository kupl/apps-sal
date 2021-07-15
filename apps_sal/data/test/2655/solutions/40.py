N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

ans = 0
cnt = 1
# 最大値は一回だけ
ans += A[0]

# N-2個は、2,2,3,3,..i,i,...のように取る
flag = False
for i in range(1, len(A)-1):
    ans += A[cnt]
    if flag == False:
        flag = True
    else:
        flag = False
        cnt += 1
print(ans)
