import math


def colcu(bli, ali, D):
    num = 0
    for i in range(D):
        num += (bli[i] - ali[i]) ** 2
    return math.sqrt(num)


N, D = map(int, input().split())
pli = []
for i in range(N):
    pli.append(list(map(int, input().split())))

an = 0
for i in range(N - 1):
    for t in range(i + 1, N):
        if colcu(pli[i], pli[t], D).is_integer():
            an += 1
print(an)
