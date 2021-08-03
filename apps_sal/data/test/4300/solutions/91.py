N = int(input())
d_list = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(i):
        ans += d_list[i] * d_list[j]
print(ans)
