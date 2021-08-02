n = int(input())
l = tuple(map(int, input().split()))
r = tuple(map(int, input().split()))
s = [(i, sum(v)) for i, (v) in enumerate(zip(l, r))]
ss = sorted(s, key=lambda a: a[1])

candies = [0] * n
for p in ss:
    candies[p[0]] = n - p[1]

ll = [0]
for i in range(1, n):
    ll.append(sum([1 for c in candies[:i] if c > candies[i]]))

rr = [0]
for i in range(n - 2, -1, -1):
    rr.append(sum([1 for c in candies[i:] if c > candies[i]]))

for i in range(n):
    if ll[i] != l[i]:
        print("NO")
        break
    if rr[n - 1 - i] != r[i]:
        print("NO")
        break
    if i == n - 1:
        print("YES")
        print(' '.join(map(str, candies)))
