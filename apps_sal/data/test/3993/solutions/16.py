(n, m, k) = map(int, input().split())
a = sorted(map(int, input().split()))
d = 0
i = 0
t = 0
while i < len(a):
    p = (a[i] - d - 1) // k
    j = i
    while j < len(a) and (a[j] - d - 1) // k == p:
        j = j + 1
    d = d + j - i
    t = t + 1
    i = j
print(t)
