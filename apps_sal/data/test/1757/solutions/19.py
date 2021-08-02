n = int(input())
fib = [1]
a = 1
b = 1
for i in range(0, 1000):
    b = a + b
    fib.append(b)
    if b > 1000:
        break
    a, b = b, a

s = ""

for i in range(1, n + 1):
    if i in fib:
        s += 'O'
    else:
        s += 'o'

print(s)
