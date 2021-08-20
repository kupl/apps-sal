(n, t) = list(map(int, input().split()))
l = list(map(int, input().split()))
s = 0
for i in range(len(l) - 1):
    s += min(t, l[i + 1] - l[i])
s += t
print(s)
