n, k = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())

for i in range(n - k):
    if T[i] == T[i + k]:
        T[i + k] = ""

ans = 0
for i in range(n):
    if T[i] == "r":
        ans += P
    if T[i] == "s":
        ans += R
    if T[i] == "p":
        ans += S

print(ans)
