a, b = map(int, input().split())
x = abs(b + a)
if(x % 2 != 0):
    print("IMPOSSIBLE")
else:
    print(int(x / 2))
