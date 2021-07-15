from math import sqrt

def f(sa, sb, sc, sd, A, B, C, D):
    cA = sa * sd - sb * sc
    cB = sa * D + sd * A - sb * C - sc * B
    cC = A * D - B * C
    if cA == 0:
        if cB == 0:
            return 0 if cC == 0 else float("inf")
        return abs(-cC / cB)
    return float("inf")

def main():
    import sys
    
    A, B, C, D = [int(i) for i in sys.stdin.read().split()]
    result = float("inf")
    for sa in [-1, 1]:
        for sb in [-1, 1]:
            for sc in [-1, 1]:
                for sd in [-1, 1]:
                    result = min(result, f(sa, sb, sc, sd, A, B, C, D))
    
    print(result)
    
    
main()
