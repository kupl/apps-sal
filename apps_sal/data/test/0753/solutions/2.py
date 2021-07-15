import fractions

def solve(a, b, c, d):
    if a * d == b * c:
        return "0/1"
    elif a / c > b / d:
        return str(fractions.Fraction(a * d - c * b, a * d))
    else:
        return str(fractions.Fraction(c * b - a * d, c * b))

def test():
    assert solve(1, 1, 3, 2) == "1/3"
    assert solve(4, 3, 2, 2) == "1/4"
    assert solve(1, 1, 1, 1) == "0/1"
    print("test passes")

##test()
a, b, c, d = tuple(map(int, input().split()))
print(solve(a, b, c, d))
    

