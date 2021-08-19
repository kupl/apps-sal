l = list(map(int, input().split()))
a = l[0]
b = l[1]
if a > 9 or a < 1 or b > 9 or (b < 1):
    print(-1)
else:
    print(a * b)
