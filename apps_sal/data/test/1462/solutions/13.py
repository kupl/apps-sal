(n, k) = map(int, input().split())
s = list(input())
a = [0 for i in range(26)]
for i in s:
    a[ord(i) - ord('A')] += 1
a.sort()
a.reverse()
i = 0
s = 0
while k != 0:
    if a[i] <= k:
        s += a[i] * a[i]
        k -= a[i]
    else:
        s += k * k
        k = 0
    i += 1
print(s)
