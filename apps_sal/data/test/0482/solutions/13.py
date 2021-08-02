n, k = map(int, input().split())
s = ''
x = n // k
y = n % k
for i in range(x):
    for j in range(k):
        p = str(chr(97 + j))
        s = s + p
for i in range(y):
    p = str(chr(97 + i))
    s = s + p
print(s)
