from collections import Counter
def main():
    n = int(input())
    A = list(map(int, input().split()))
    c = Counter(A)
    B = sorted([(k, v) for k, v in list(c.items()) if v >= 2], reverse = True, key = lambda x: x[0])
    if len(B) < 2:
        print((0))
    elif B[0][1] >= 4:
        print((B[0][0] ** 2))
    else:
        print((B[0][0] * B[1][0]))

def __starting_point():
    main()

__starting_point()
