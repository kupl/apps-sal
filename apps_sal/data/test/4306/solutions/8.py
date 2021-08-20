t = [0] * 101
(a, b, c, d) = list(map(int, input().split()))
for i in range(a, b):
    t[i] += 1
for j in range(c, d):
    t[j] += 1
print(t.count(2))
