n, m, k = (int(x) for x in input().split())
a = [int(x) for x in input().split()]
a.sort()
a.reverse()
if k >= m:
    print(0)
    return
for i, x in enumerate(a):
    k += x - 1
    if k >= m:
        print(i + 1)
        return
print(-1)
