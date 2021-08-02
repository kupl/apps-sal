n = int(input())
a = 0
i = 1
while i * i < n:
    if n % i == 0:
        a += 2
    i += 1
if i * i == n:
    a += 1
print(a)
