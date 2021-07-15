n = int(input())
c = 0
i = 1
s = set()
while i * i <= n:
    if n % i == 0:
        s.add(i)
        s.add(n // i)
    i += 1
print(len(s))

