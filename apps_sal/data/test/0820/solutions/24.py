n = int(input())
m = int(input())
a = []
counter = 0

for i in range(n):
    a.append(int(input()))

a.sort()

for i in reversed(a):
    if m > 0:
        m -= i
        counter += 1

print(counter)
