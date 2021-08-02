n = int(input())
c = list(map(int, input().split()))
t = list(map(int, input().split()))
v = []
v1 = []
if c[0] != t[0] and c[n - 1] != t[n - 1]:
    print('No')
else:
    for _ in range(n - 1):
        v.append(c[_ + 1] - c[_])
        v1.append(t[_ + 1] - t[_])
    v.sort()
    v1.sort()
    if v != v1:
        print('No')
    else:
        print('Yes')
