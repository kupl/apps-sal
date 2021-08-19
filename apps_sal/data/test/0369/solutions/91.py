import sys
import heapq


def main():
    input = sys.stdin.readline
    (n, m) = map(int, input().split())
    s = input()
    inf = pow(10, 6)
    ans = [inf] * (n + 1)
    key = []
    heapq.heapify(key)
    heapq.heappush(key, (0, n))
    ans[n] = 0
    index = n - 1
    count = 0
    while key:
        sub = heapq.heappop(key)
        (s1, s2) = (sub[0], sub[1])
        if s1 < count:
            continue
        count = s1 + 1
        subindex = index
        for i in range(min([index, s2 - 1]), max([-1, s2 - m - 1]), -1):
            if ans[i] != inf:
                continue
            if s[i] == '1':
                continue
            heapq.heappush(key, (count, i))
            ans[i] = s2
            subindex = i
        index = subindex
    if ans[0] == inf:
        print(-1)
    else:
        index = 0
        answer = []
        while True:
            subindex = ans[index]
            answer.append(subindex - index)
            if subindex == n:
                break
            index = subindex
        print(*answer)


def __starting_point():
    main()


__starting_point()
