a, b, x = map(int, input().split())
if x - a < 0:
    print("NO")
else:
    print(("NO", "YES")[x - a <= b])
