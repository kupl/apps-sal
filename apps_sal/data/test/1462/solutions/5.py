n, k = list(map(int, input().split()))
s = input()
a = [0] * 26
for i in s:
    a[ord(i) - ord("A")] += 1
a.sort()
a = a[::-1]
i = 0
b = []
k1 = k
while i < n and k1 > 0:
    b.append(min(k1, a[i]))
    k1 -= a[i]
    i += 1
ans = 0
for i in b:
    ans += i * i
print(ans)

