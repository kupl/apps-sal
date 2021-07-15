n = int(input())
a = list(map(int, input().split()))
m = int(input())
res = []
for i in range(m):
    k, pos = map(int, input().split())
    mas1 = []
    for j in range(n):
        mas1.append(a[j])
    mas2 = sorted(mas1)
    mas1.reverse()
    for j in range(n-k):
        mas1.remove(mas2[j])
    mas1.reverse()
    res.append(mas1[pos - 1])
for i in range(m):
    print(res[i])
