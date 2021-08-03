def solve(n, A, B):
    if A == sorted(A):
        return True
    if len(set(B)) == 2:
        return True
    return False


def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        print("Yes" if solve(n, A, B) else "No")


def __starting_point():
    main()


__starting_point()
