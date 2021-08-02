n, k = list(map(int, input().split()))
d = [0] * (k + 1)
for i in range(n):
    d[(int(input()))] += 1
r = 0
ans = 0
for i in d:
    ans += (i // 2) * 2
    r += i % 2
print(ans + -(-r // 2))
