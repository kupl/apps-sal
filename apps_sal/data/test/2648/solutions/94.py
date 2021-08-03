n = int(input())
a = list(map(int, input().split()))

b = len(set(a))
if b % 2 == 1:
    print(b)
else:
    print((b - 1))
