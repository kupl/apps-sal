x = int(input())
def f(x):
    x += 1
    while x % 10 == 0:
        x //= 10
    return x
d = set()
while not x in d:
    d.add(x)
    x = f(x)
print(len(d))
