import sys
sys.setrecursionlimit(10**9)


def mi(): return map(int, input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))


INF = 10**20


def main():
    N, M = mi()
    A = list(mi())

    v = [0] * 2 * 10**5
    seen = set([0])
    for i in range(N):
        v[i + 1] = A[i] + v[i]
        v[i + 1] %= M
        seen.add(v[i + 1])

    counts = {x: 0 for x in seen}
    for i in range(N + 1):
        counts[v[i]] += 1

    ans = 0
    for _, count in counts.items():
        ans += count * (count - 1) // 2

    print(ans)


def __starting_point():
    main()


__starting_point()
