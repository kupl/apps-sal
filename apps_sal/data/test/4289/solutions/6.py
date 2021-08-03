a = int(input())
b, c = list(map(int, input().split()))
d = list(map(int, input().split()))
e = []
f = []
ans = 10**9
for i in d:
    e.append(b - 0.006 * i)
for j in e:
    f.append(abs(c - j))
print((f.index(min(f)) + 1))
