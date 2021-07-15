from sys import stdin, stdout # only need for big input


def solve():
    c1 = list(map(int, input().split()))
    c2 = list(map(int, input().split()))
    c3 = list(map(int, input().split()))
    b = c1
    a2 = [c2[i] - b[i] for i in range(3)]
    a3 = [c3[i] - b[i] for i in range(3)]
    if max(a2) == min(a2) and max(a3) == min(a3):
        print("Yes")
    else:
        print("No")

def main():
    solve()


def __starting_point():
    main()
__starting_point()
