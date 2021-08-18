
from fractions import gcd

try:
    while True:
        n = int(input())
        a = list(map(int, input().split()))
        result = [a[0]]
        for x in a[1:]:
            if gcd(x, result[-1]) != 1:
                result.append(1)
            result.append(x)
        print(len(result) - len(a))
        print(' '.join(map(str, result)))

except EOFError:
    pass
