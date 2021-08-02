n = int(input())

seq = sorted(list(map(int, input().split())))

ans = 0
for i in range(0, n, 2):
    ans += seq[i + 1] - seq[i]
print(ans)
