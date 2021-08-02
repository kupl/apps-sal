n, k, m = list(map(int, input().split()))
a = list(input().split())

b = list(map(int, input().split()))
while k:
    k -= 1
    o = list(input().split())
    x = int(o[0])
    c = list(map(int, o[1:]))
    mini = min([b[i - 1] for i in c])
    for i in c:
        b[i - 1] = mini
p = list(input().split())
ma = {}
for i in range(len(a)):
    ma[a[i]] = b[i]
s = 0
for i in p:
    s += ma[i]
print(s)
