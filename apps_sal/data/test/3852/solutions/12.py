import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def in_n(): return int(readline())
def in_nn(): return list(map(int, readline().split()))
def in_s(): return readline().rstrip().decode('utf-8')
def in_nl(): return list(map(int, readline().split()))
def in_nl2(H): return [in_nl() for _ in range(H)]
def in_map(): return [s == ord('.') for s in readline() if s != ord('\n')]
def in_map2(H): return [in_map() for _ in range(H)]
def in_all(): return list(map(int, read().split()))


def main():

    N = in_n()
    A = in_nl()

    ans = []
    if abs(min(A)) < abs(max(A)):
        ma = max(A)
        ind = A.index(ma)
        for i in range(N):
            if i != ind:
                ans.append((ind + 1, i + 1))
                A[i] += A[ind]
    else:
        ma = min(A)
        ind = A.index(ma)
        for i in range(N):
            if i != ind:
                ans.append((ind + 1, i + 1))
                A[i] += A[ind]

    if min(A) >= 0:
        for i in range(N - 1):
            if A[i] > A[i + 1]:
                max_a = max(A)
                ind = A.index(max_a)
                A[i + 1] += max_a
                ans.append((ind + 1, i + 2))
    else:
        for i in range(N - 1, 0, -1):
            if A[i - 1] > A[i]:
                min_a = min(A)
                ind = A.index(min_a)
                A[i - 1] += min_a
                ans.append((ind + 1, i))

    print((len(ans)))
    for x, y in ans:
        print((x, y))

    # print(A)


def __starting_point():
    main()


__starting_point()
