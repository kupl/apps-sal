N = int(input())
D = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}
for i in range(N):
    D[input()] += 1
for x, y in list(D.items()):
    print(("{0} x {1}".format(x, y)))


