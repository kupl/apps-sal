n = int(input())
a = [0]

while n > 2 * (a[-1] + 1):
    n -= a[-1] + 1
    a.append(a[-1] + 1)

if n != 0:
    a.append(n)

a.remove(0)

print(len(a))
print(*a)
