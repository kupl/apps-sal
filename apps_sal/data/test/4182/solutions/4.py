n, m, x, y = list(map(int, input().split()))
xn = list(map(int, input().split()))
yn = list(map(int, input().split()))
maxx = max(xn)
miny = min(yn)
if x < miny and miny <= y and miny > maxx:
    print("No War")
else:
    print("War")
