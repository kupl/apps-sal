import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
def int1(x): return int(x) - 1


def main():
    n, a, b = list(map(int, input().split()))
    if not (n + a - 1) // a <= b <= n - a + 1:
        print((-1))
        return
    ans = []
    ans.append(list(range(1, a + 1)))
    b -= 1
    st = a + 1
    while b:
        if b == 1:
            ans.append(list(range(st, n + 1)))
            break
        elif n - st + 1 - a >= b - 1:
            ans.append(list(range(st, st + a)))
            st += a
            b -= 1
        else:
            ans.append([st])
            st += 1
            b -= 1
    x = []
    for ak in ans[::-1]:
        x += ak
    print((*x))


main()
