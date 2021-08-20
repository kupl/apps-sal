(n, B) = (int(x) for x in input().split())
a = [int(x) for x in input().split()]
odd = 0
s = []
for i in range(n - 1):
    if a[i] % 2 == 1:
        odd += 1
    else:
        odd -= 1
    if odd == 0:
        s.append(abs(a[i] - a[i + 1]))
s.sort()
k = 0
i = 0
while i < len(s) and k + s[i] <= B:
    k += s[i]
    i += 1
print(i)
