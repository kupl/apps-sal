x, y = list(map(int, input().split()))

ga = [4, 6, 9, 11]
gb = [1, 3, 5, 7, 8, 10, 12]
gc = [2]

xg = yg = ""


def group(x):
    if x in ga:
        return "ga"
    if x in gb:
        return "gb"
    if x in gc:
        return "gc"


xg = group(x)
yg = group(y)
if xg == yg:
    print("Yes")
else:
    print("No")
