from bisect import bisect_right


def main():
    inf = float("inf")
    n = int(input())
    alst = [int(input()) for _ in range(n)]
    work = [inf] * n
    for i in range(n - 1, -1, -1):
        j = bisect_right(work, alst[i])
        work[j] = alst[i]
    print(n - work.count(inf))


main()
