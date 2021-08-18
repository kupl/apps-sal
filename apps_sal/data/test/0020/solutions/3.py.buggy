h, m = map(int, input().split(':'))


def increment():
    nonlocal m, h
    m += 1
    h += m // 60
    m %= 60
    h %= 24


def reverse(num):
    return num % 10 * 10 + num // 10


ans = 0
while h != reverse(m):
    increment()
    ans += 1

print(ans)
