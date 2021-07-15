def f(x):
    x += 1
    while not x % 10:
        x //= 10
    return x


previous = set()

n = int(input())
while n not in previous:
    previous.add(n)
    n = f(n)

print(len(previous))

