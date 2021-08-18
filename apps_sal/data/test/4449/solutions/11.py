
import sys

q = int(input())

for i in range(0, q):
    n = int(input())
    ln = [int(j) for j in sys.stdin.readline().rstrip().split(" ")]
    ln = sorted(ln)
    f = True
    for j in range(1, len(ln), 2):
        if ln[j] != ln[j - 1]:
            f = False

    ind1 = 0
    ind2 = len(ln) - 2
    sm = ln[ind1] * ln[ind2]
    while ind1 < ind2:
        ind1 += 2
        ind2 -= 2
        if ln[ind1] * ln[ind2] != sm:
            f = False
            break
    if f:
        print("YES")
    else:
        print("NO")
