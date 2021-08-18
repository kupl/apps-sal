import heapq
n = int(input())
a = list(map(int, input().split()))


lefts = a[:n]
lefts_sums = [sum(lefts)]
heapq.heapify(lefts)

for x in range(n, 2 * n):
    l = heapq.heappop(lefts)
    if l < a[x]:
        heapq.heappush(lefts, a[x])
        lefts_sums.append(lefts_sums[-1] - l + a[x])
    else:
        heapq.heappush(lefts, l)
        lefts_sums.append(lefts_sums[-1])

rights = [-_a for _a in a[2 * n:]]
rights_sums = [sum(rights)]
heapq.heapify(rights)

for x in reversed(list(range(n, 2 * n))):
    r = heapq.heappop(rights)
    if r < -a[x]:
        heapq.heappush(rights, -a[x])
        rights_sums.append(rights_sums[-1] - r - a[x])
    else:
        heapq.heappush(rights, r)
        rights_sums.append(rights_sums[-1])

rights_sums = rights_sums[::-1]
ans = -float('inf')
for i in range(len(lefts_sums)):
    ans = max(ans, lefts_sums[i] + rights_sums[i])
print(ans)
