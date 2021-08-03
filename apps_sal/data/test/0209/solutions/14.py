sa = input().split(' ')
x = int(sa[0])
y = int(sa[1])
n = int(input())


def generate(x, y, n):
    sa = [x, y, y - x, -x, -y, x - y]
    return sa[((n % 6) - 1) % 6]


print(generate(x, y, n) % (10**9 + 7))
