from collections import deque
import heapq


def main():
    from sys import stdin
    lines = deque((line.strip() for line in stdin.readlines()))
    (n, k) = [int(x) for x in lines.popleft().split()]
    temps = deque((int(x) for x in lines.popleft().split()))
    temps.appendleft(0)
    streaks = []
    count = 0
    ispositive = True
    numnegative = 0
    changes = 0
    while temps:
        temp = temps.popleft()
        positive = temp >= 0
        if positive:
            count += 1
            if not ispositive:
                changes += 1
        else:
            numnegative += 1
            if ispositive:
                streaks.append(count)
                count = 0
                changes += 1
        ispositive = positive
    if numnegative == 0:
        print(0)
        return
    if numnegative > k:
        print(-1)
        return
    if k >= n:
        print(1)
        return
    k -= numnegative
    heap = streaks[1:]
    heapq.heapify(heap)
    heap2 = list(heap)
    if ispositive:
        heapq.heappush(heap2, count)
    changes2 = changes
    k2 = k
    while heap and k >= heap[0]:
        k -= heapq.heappop(heap)
        changes -= 2
    if ispositive and k > count:
        changes -= 1
    while heap2 and k2 >= heap2[0]:
        k2 -= heapq.heappop(heap2)
        changes2 -= 2
    if ispositive and (not heap2 or heap2[0] > count):
        changes2 += 1
    print(min(changes, changes2))


def __starting_point():
    main()


__starting_point()
