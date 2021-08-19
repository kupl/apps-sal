n = int(input())
a = list(map(int, input().split()))
d = dict()
d[0] = 0
mx = 0
for i in a:
    d[i] = d.get(i, 0) + 1
    if d[i] > d[mx]:
        mx = i
print(mx)
