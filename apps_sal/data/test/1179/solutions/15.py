s = input().split()
(n, k) = (int(s[0]), int(s[1]))
id = list(map(lambda x: int(x), input().split()))
c = 1
d = 1
while c + d <= k:
    c += d
    d += 1
print(id[k - c])
