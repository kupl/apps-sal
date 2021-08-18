
n = int(input())
T = sorted(list(map(int, input().split())))

total_time = 0
ans = 0
for i in range(n):
    if total_time <= T[i]:
        total_time += T[i]
        ans += 1
print(ans)
