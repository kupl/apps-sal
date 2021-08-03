
n = int(input())
a = list(map(int, input().split()))
b = sorted(a)

prefa = [0] * (n + 1)
prefb = [0] * (n + 1)

for i in range(1, n + 1):
    prefa[i] = prefa[i - 1] + a[i - 1]

for i in range(1, n + 1):
    prefb[i] = prefb[i - 1] + b[i - 1]

m = int(input())
for i in range(m):
    type, l, r = map(int, input().split())
    if type == 1:
        print(prefa[r] - prefa[l - 1])
    else:
        print(prefb[r] - prefb[l - 1])
