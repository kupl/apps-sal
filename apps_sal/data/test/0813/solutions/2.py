n, a, b = tuple(map(int, str.split(input())))
a_s = set(map(int, str.split(input())))
b_s = set(map(int, str.split(input())))

def yoba(n, a_s, b_s):

    for i in range(1, n + 1):

        yield 1 if i in a_s else 2

print(str.join(" ", list(map(str, yoba(n, a_s, b_s)))))

