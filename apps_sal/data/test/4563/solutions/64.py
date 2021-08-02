def nextpt(ratio1, ratio2, pt):
    if ratio1[0] * ratio2[1] - ratio1[1] * ratio2[0] > 0:
        pt[0] = pt[0] + ((-1) * pt[0]) % ratio2[0]
        pt[1] = pt[0] * ratio2[1] // ratio2[0]
    else:
        pt[1] = pt[1] + ((-1) * pt[1]) % ratio2[1]
        pt[0] = pt[1] * ratio2[0] // ratio2[1]
    return pt


n = int(input())
ratios = [list(map(int, input().split())) for _ in range(n)]

pt = ratios[0]
for i in range(n - 1):
    pt = nextpt(ratios[i], ratios[i + 1], pt)

print(sum(pt))
