import sys
for _ in range(int(input())):
    a, b = map(int, input().split())
    res = a * (len(str(b + 1)) - 1)
    print(res)
