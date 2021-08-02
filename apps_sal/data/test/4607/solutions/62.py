a, b = map(int, input().split())
if 1 <= b < a:
    print(a - 1)
elif a <= b:
    print(a)
