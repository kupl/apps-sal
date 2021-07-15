n = int(input())
arr = list(map(int, input().split()))
d = {}
for i in arr:
    c = bin(i).count('1')
    d[c] = d.get(c, 0) + 1
res = [v * (v - 1) // 2 for v in list(d.values())]
print(sum(res))

