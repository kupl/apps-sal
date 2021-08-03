n, k = map(int, input().split())
a = [int(x) - 1 for x in input().split()]
s = [0] * 100
for i in range(n):
    s[a[i]] += 1
m = max(s)
if m % k != 0:
    m += k - m % k
print(sum([m - s[i] for i in range(100) if s[i] != 0]))
