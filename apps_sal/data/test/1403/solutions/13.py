s = input()
(n, K) = list(map(int, s.split()))
s = input()
a = list(map(int, s.split()))
a = sorted(a)
c = 0
l = 0
r = 1
while r < len(a):
    if a[r] == a[l]:
        r += 1
    else:
        if a[l] + K >= a[r]:
            c += r - l
        l = r
        r += 1
print(len(a) - c)
