(n, k) = map(int, input().split())
S = input()
dif = 1
for i in range(0, n - 1):
    if S[i] != S[i + 1]:
        dif += 1
print(n - max(1, dif - 2 * k))
