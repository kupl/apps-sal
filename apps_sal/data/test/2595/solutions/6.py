import sys
input = sys.stdin.readline
for _ in range(int(input())):
    (a, b) = map(int, input().split())
    if a > b:
        (a, b) = (b, a)
    res = 0
    while a < b:
        if a * 8 <= b:
            a *= 8
        elif a * 4 <= b:
            a *= 4
        else:
            a *= 2
        res += 1
    if a == b:
        print(res)
    else:
        print(-1)
