x, a, b = map(int, input().split())
ar = abs(x - a)
br = abs(x - b)

if br < ar:
    print("B")
elif br > ar:
    print("A")
