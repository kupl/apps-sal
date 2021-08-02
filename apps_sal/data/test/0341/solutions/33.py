n, k = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())

for i in range(n - k):
    if T[i] == T[i + k]:
        T[i + k] = 0

ans = [0] * n
for i in range(n):
    if T[i] == "r":
        ans[i] = P
    if T[i] == "s":
        ans[i] = R
    if T[i] == "p":
        ans[i] = S

print(sum(ans))
