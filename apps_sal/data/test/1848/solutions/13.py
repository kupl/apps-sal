n = int(input())
pictures = list(map(int, input().split()))
d = dict()
for i in pictures:
    d[i] = 0
for i in pictures:
    d[i] += 1
a = sorted(d.values())
i = 1
r = 0
l = len(a) - 1
s = 0
while i < len(a):
    c = i
    while i < len(a) and a[i] == a[i - 1]:
        i += 1
    s += l * (a[i - 1] - r)
    l -= i - c + 1
    r = a[i - 1]
    i += 1
print(s)
