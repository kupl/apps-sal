s = input()
p = int(s.split()[1])
s = input()
n = int(len(s))
a = []
if p > n // 2:
    p = n - p + 1
sum = 0
if n == 1:
    print('0')
    quit()
for i in range(n // 2):
    j = int(n - i - 1)
    q = abs(ord(s[j]) - ord(s[i]))
    a.append(min(q, 26 - q))
    sum += a[i]
i = 0
while (a[i] == 0) & (i < p - 1):
    i += 1
if i == p - 1:
    i = 0
else:
    i = p - i - 1
j = n // 2 - 1
while (a[j] == 0) & (j > p - 1):
    j -= 1
if j == p - 1:
    j = 0
else:
    j = j - p + 1
sum += min(i, j) * 2 + max(i, j)
print(str(sum))
