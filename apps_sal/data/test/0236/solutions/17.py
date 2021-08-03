def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


s = input().strip()
a = s.count('-')
b = s.count('o')
if b:
    print('YES' if a % b == 0 else 'NO')
else:
    print('YES')
