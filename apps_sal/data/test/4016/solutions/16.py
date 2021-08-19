(n, k) = map(int, input().split())
t = input()
P = [0] * n
for i in range(1, n):
    j = P[i - 1]
    while t[j] != t[i] and j > 0:
        j = P[j - 1]
    if t[i] == t[j]:
        j += 1
    P[i] = j
ans = t[:n - P[n - 1]] * k
if P[n - 1] > 0:
    ans += t[n - P[n - 1]:]
print(ans)
