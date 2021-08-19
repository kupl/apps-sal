n = int(input())
a = [0]
b = input().split()
a = a + b
ans = 0
m = 0
for i in range(1, n + 1):
    a[i] = int(a[i])
(s, f) = input().split()
s = int(s)
f = int(f)
for i in range(s, f):
    m += a[i]
ma = m
ans = 1
start = s - 1
count = f - 1
if count < 1:
    count = n
if start < 1:
    start = n
for i in range(2, n + 1):
    m = m - a[count] + a[start]
    count = count - 1
    start = start - 1
    if count == 0:
        count = n
    if start == 0:
        start = start = n
    if m > ma:
        ma = m
        ans = i
print(ans)
