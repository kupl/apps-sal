input()
ds = str.strip(input())
xs = list(map(int, str.split(input())))


best = None
last_right = None
for d, x in zip(ds, xs):

    if d == "R":

        last_right = x

    elif last_right is not None:

        t = (x - last_right) // 2
        best = min(best or t, t)

print(best or -1)

