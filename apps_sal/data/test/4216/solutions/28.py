n = int(input())
l = []
i = 1
while i * i <= n:
    if n % i == 0:
        num = max(len(str(i)), len(str(n // i)))
        l.append(num)
    i += 1
print(min(l))
