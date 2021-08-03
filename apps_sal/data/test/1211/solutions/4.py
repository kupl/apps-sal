a, b = map(int, input().split())
k = list(map(int, input().split()))
s = []
for i in range(b):
    s += [[a % k[i], i + 1, a // k[i]]]
s.sort()
print(s[0][1], s[0][2])
