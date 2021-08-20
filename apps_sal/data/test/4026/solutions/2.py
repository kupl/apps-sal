def solve():
    (n, m) = list(map(int, input().split()))
    found = False
    for _ in range(n):
        (a, b) = list(map(int, input().split()))
        (c, d) = list(map(int, input().split()))
        if b == c:
            found = True
    if m % 2 == 1:
        return False
    if found:
        return True
    return False


t = int(input())
for _ in range(t):
    if solve():
        print('YES')
    else:
        print('NO')
