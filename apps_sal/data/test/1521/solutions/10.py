p, n = map(int, input().split())
x = [0 for i in range(n)]
for i in range(n):
    x[i] = int(input())
was = [0 for i in range(p)]
k = -1
for i in range(n):
    if was[x[i] % p]:
        k = i + 1
        break
    else:
        was[x[i] % p] = 1
print(k)
