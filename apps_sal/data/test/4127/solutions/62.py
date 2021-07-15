def main(A, B):
    B = round(100 * B)
    ans = A * B
    return int(ans // 100)


def __starting_point():
    A, B = input().split()
    A = int(A)
    B = float(B)
    ans = main(A, B)
    print(ans)

__starting_point()
