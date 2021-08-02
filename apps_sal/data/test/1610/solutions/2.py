n, k = map(int, input().split())

L = list(range(1, n + 1))
if(k != 0):
    i = -k + n
    s = L[-k:-1] + [L[-1]]
    s.reverse()
    L = s + L[:i]

for i in range(n - 1):
    print(L[i], end=" ")

print(L[-1])
