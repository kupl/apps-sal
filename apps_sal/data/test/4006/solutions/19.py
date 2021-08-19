n = int(input())
s = set()
s.add(n)
while n != 1:
    n = n + 1
    while n % 10 == 0:
        n = n // 10
    s.add(n)
for i in range(2, 10):
    s.add(i)
print(len(s))
