n, q = list(map(int, input().split()))
a = [int(i) for i in input().split()]
p = min(a)
z = max(a)
for i in range(q):
    t = int(input())
    if p <= t <= z:
        print('Yes')
    else:
        print('No')
