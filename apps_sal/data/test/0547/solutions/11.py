
n, k = map(int, input().split())
S = [str(input()) for _ in range(n)]
p = str(input())

L = [len(S[i]) for i in range(n)]
lp = len(p)

L.sort()
ok = 0
for i in range(n):
    if L[i] == lp and ok == 0:
        ok = 1
        print(i + 1 + i // k * 5, end=" ")
    if L[i] > lp:
        print(i + (i - 1) // k * 5)
        ok = 2
        break
if ok == 1:
    print(n + (n - 1) // k * 5)
