def inp():
    return map(int, input().split(' '))


def is_tr(a, b, c):
    if a < b + c:
        if b < a + c:
            if c < b + a:
                return True
    return False


n = int(input())
a = list(inp())
a.sort()

for i in range(n - 2):
    if is_tr(a[i], a[i + 1], a[i + 2]):
        print('YES')
        return
print('NO')
