x = int(input())
seen = set()


def f(x):
    x += 1
    while x % 10 == 0:
        x = x // 10
    return x


while x not in seen:
    seen.add(x)
    x = f(x)
print(len(seen))
