import sys
A, B, C, D = [int(i) for i in sys.stdin.read().split()]
if A * D - B * C == 0:
    result = 0
else:
    result = float("inf")
    for sa in [-1, 1]:
        for sb in [-1, 1]:
            for sc in [-1, 1]:
                for sd in [-1, 1]:
                    coefA = sa * sd - sb * sc
                    coefB = sa * D + sd * A - sb * C - sc * B
                    coefC = A * D - B * C
                    if coefA == 0 and coefB != 0:
                        v = -coefC / coefB
                        result = min(result, abs(v))
print(result)
