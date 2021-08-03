x, a, b = map(int, input().split())
if min(abs(x - a), abs(x - b)) == abs(x - a):
    print("A")
else:
    print("B")
