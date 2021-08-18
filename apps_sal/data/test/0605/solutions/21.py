def score(p, t):
    return max(3 * p / 10, p - p / 250 * t)


inData = input().split()
numb = [int(x) for x in inData]
mishaRes = score(numb[0], numb[2])
vasyaRes = score(numb[1], numb[3])
if mishaRes == vasyaRes:
    print("Tie")
elif mishaRes > vasyaRes:
    print("Misha")
else:
    print("Vasya")
