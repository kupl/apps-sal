def kk(): return map(int, input().split())
# k2=lambda:map(lambda x:int(x)-1, input().split())
def ll(): return list(kk())


n, t = kk()
mv, j = 10000000000, -1
for i in range(n):
    s, d = kk()
    while s < t:
        s += d
    if s < mv:
        mv, j = s, i
print(j + 1)
