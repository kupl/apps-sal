from sys import stdin
n = int(stdin.readline().strip())
s = list(map(int, stdin.readline().strip().split()))
s.sort()
ans = 10 ** 20
t1 = -1
for t in range(1, 101):
    aux1 = 0
    for j in range(n):
        aux = 102
        aux = min(aux, abs(1 + t - s[j]))
        aux = min(aux, abs(t - 1 - s[j]))
        aux = min(aux, abs(t - s[j]))
        aux1 += aux
    if aux1 < ans:
        ans = aux1
        t1 = t
print(t1, ans)
