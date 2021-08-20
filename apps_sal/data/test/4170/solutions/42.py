N = int(input())
H_list = list(map(int, input().split()))
cnt = 0
ans = 0
for i in range(N - 1):
    if H_list[i] >= H_list[i + 1]:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)
print(ans)
