n, k, q = map(int, input().split())

x = [0] * 200005

for _ in range(n):
    l, r = map(int, input().split())

    x[l] += 1
    x[r+1] -= 1

for i in range(1,200005):
    x[i] += x[i-1]
    x[i-1] = [0,1][x[i-1]>=k]

for i in range(1,200005):
    x[i] += x[i-1]

res = ''

for _ in range(q):
    l, r = map(int, input().split())

    res += str(x[r]-x[l-1]) + "\n"

print(res, end='')

