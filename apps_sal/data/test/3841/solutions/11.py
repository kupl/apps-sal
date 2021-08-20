(p, k) = map(int, input().split())
l = []
while p:
    l.append((p % k + k) % k)
    p = (p % k - p) // k
print(len(l))
for i in l:
    print(i, end=' ')
