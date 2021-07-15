from itertools import permutations

n, k = list(map(int, input().split()))
ans = 0
cur = 4 * 60 - k
for i in range(1, n + 1):
    if cur < 5 * i:
        break
    cur -= 5 * i
    ans += 1

print(ans)

