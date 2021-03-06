import sys
import heapq
input = sys.stdin.readline


def main():
    N = int(input())
    S = [[x for x in input().split()] for _ in range(2 * N)]
    q = []
    ans = []
    for s in S[::-1]:
        if s[0] == '-':
            heapq.heappush(q, int(s[1]))
        elif q:
            c = heapq.heappop(q)
            ans.append(c)
        else:
            print('NO')
            return
    ans2 = ans[::-1]
    q = []
    current = 0
    for s in S:
        if s[0] == '-':
            c = heapq.heappop(q)
            if c != int(s[1]):
                print('NO')
                return
        else:
            heapq.heappush(q, ans2[current])
            current += 1
    print('YES')
    print(*ans2)


def __starting_point():
    main()


__starting_point()
