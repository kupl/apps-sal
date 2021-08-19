N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
ans = 0
cnt = 1
ans += A[0]
flag = False
for i in range(1, len(A) - 1):
    ans += A[cnt]
    if flag == False:
        flag = True
    else:
        flag = False
        cnt += 1
print(ans)
