h1, a1, c1 = map(int, input().split())
h2, a2 = map(int, input().split())

a = []

while True:
    if h2 <= a1 or h1 > a2:
        h2 -= a1
        a += ["STRIKE"]
    else:
        h1 += c1
        a += ["HEAL"]

    if h2 <= 0:
        break
    h1 -= a2
print(len(a))
for x in a:
    print(x)
