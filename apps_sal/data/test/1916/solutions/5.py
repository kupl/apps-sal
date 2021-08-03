c = 0
n, m = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
al.sort(key=lambda a: min([a & b for b in bl]))
al.reverse()
for a in al:
    minc = pow(10, 12)
    for b in bl:
        minc = min(minc, c | (a & b))
    c = int(minc)
print(c)
