s, t = ["v<^>".index(x) for x in input().split()]
n = int(input())

cw = (n + s - t) % 4 == 0
ccw = (n + t - s) % 4 == 0

if cw and not ccw:
    print("cw")
elif not cw and ccw:
    print("ccw")
else:
    print("undefined")
