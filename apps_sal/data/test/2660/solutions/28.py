import heapq
q = int(input())
(big, small) = ([], [])
heapq.heapify(big)
heapq.heapify(small)
sumb = 0
sumdist = 0
i = 0
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        i += 1
        (a, b) = (query[1], query[2])
        sumb += b
        if i % 2 == 1:
            if i == 1:
                median = a
            elif big[0] <= a:
                median = heapq.heappushpop(big, a)
                sumdist += abs(a - median)
            elif a <= -small[0]:
                median = -heapq.heappushpop(small, -a)
                sumdist += abs(a - median)
            else:
                median = a
        else:
            sumdist += abs(a - median)
            heapq.heappush(big, max(a, median))
            heapq.heappush(small, -min(a, median))
            median = -small[0]
    else:
        print(median, sumdist + sumb)
