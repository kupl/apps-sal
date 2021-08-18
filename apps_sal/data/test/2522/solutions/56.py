import sys
sys.setrecursionlimit(10 ** 9)
def int1(x): return int(x) - 1
def II(): return int(input())
def MI(): return list(map(int, input().split()))
def MI1(): return list(map(int1, input().split()))
def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def MS(): return input().split()
def LS(): return list(input())
def LLS(rows_number): return [LS() for _ in range(rows_number)]
def printlist(lst, k=' '): print((k.join(list(map(str, lst)))))


INF = float('inf')


def solve():
    N = II()
    A = LI()
    B = sorted(LI(), reverse=True)
    tmp = []
    for i in range(N):
        if A[i] == B[i]:
            tmp.append((i, A[i]))

    j = 0
    while tmp:
        idx, x = tmp.pop()
        for i in range(j, N):
            b = B[i]
            j = i + 1
            if i == idx:
                continue
            if b != x and x != A[i]:
                B[i], B[idx] = B[idx], B[i]
                break
        else:
            print('No')
            return
    print('Yes')
    print((*B))


def __starting_point():
    solve()


__starting_point()
