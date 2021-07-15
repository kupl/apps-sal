# input
N = int(input())
A = list(map(int, input().split()))
M = int(input())
Q = [input().split() for m in range(M)]

def solve():
    count = 0
    for i in range(N):
        for j in range(i):
            if A[i] < A[j]:
                count += 1
                count %= 2

    res = []
    for q in Q:
        l, r = q
        l = int(l) - 1
        r = int(r) - 1
        count += ((r -  l + 1)//2)
        count %= 2
        if count == 0:
            res.append('even')
        else:
            res.append('odd')

    print('\n'.join(res))

def __starting_point():
    solve()


__starting_point()
