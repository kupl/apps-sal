(n, k) = list(map(int, input().split()))
l = []
c = 0
for i in range(1, k + 1):
    l.append(n % i)
    p = set(l)
    if len(p) != len(l):
        print('No')
        c = 1
        break
if c == 0:
    print('Yes')
