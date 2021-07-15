N = int(input())
a_list = list(map(int, input().split()))

num = 1
ans = 0
for i in range(N):
    if a_list[i] != num:
        ans += 1
    else:
        num += 1
if num == 1:
    print(-1)
else:
    print(ans)
