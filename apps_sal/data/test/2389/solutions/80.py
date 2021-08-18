import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
N, A, B, C = map(int, input().split())
S = [input().strip("\n").replace("A", "0").replace("B", "1").replace("C", "2") for _ in range(N)]
Ans = [None] * N


def search(i, num):
    if i == N:
        if min(num) >= 0:
            return True
        else:
            return False
    if min(num) < 0:
        return False
    L = [num[0], num[1], num[2]]
    f = S[i][0]
    s = S[i][1]
    L[int(f)] += 1
    L[int(s)] -= 1
    if search(i + 1, L):
        Ans[i] = f
        return True
    L[int(f)] -= 2
    L[int(s)] += 2
    if search(i + 1, L):
        Ans[i] = s
        return True
    return False


def solve():
    if search(0, [A, B, C]):
        print("Yes")
        for i, a in enumerate(Ans):
            if a == "0":
                print("A")
            elif a == "1":
                print("B")
            else:
                print("C")
    else:
        print("No")

    return 0


def __starting_point():
    solve()


__starting_point()
