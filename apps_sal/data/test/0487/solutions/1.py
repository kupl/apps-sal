n = int(input())
ar = list(map(int, input().split()))
k = max(ar)
while True:
    (s1, s2) = (0, 0)
    for e in ar:
        s1 += e
        s2 += k - e
    if s2 > s1:
        break
    k += 1
print(k)
