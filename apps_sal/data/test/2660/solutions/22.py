import heapq
q = int(input())
ans = []
mini = 0
(left, right) = ([], [])
cnt = 0
mid = None
for _ in range(q):
    qi = input()
    if qi == '2':
        if cnt % 2 == 0:
            ans.append([-left[0], mini])
        else:
            ans.append([mid, mini])
    else:
        (kind, a, b) = map(int, qi.split())
        if cnt % 2 == 1:
            mini += abs(mid - a) + b
            heapq.heappush(left, -min(mid, a))
            heapq.heappush(right, max(mid, a))
            mid = None
        else:
            if cnt == 0:
                mid = a
                mini = b
                cnt += 1
                continue
            l = -heapq.heappop(left)
            r = heapq.heappop(right)
            if a <= l:
                mini += l - a + b
                heapq.heappush(left, -a)
                heapq.heappush(right, r)
                mid = l
            elif a <= r:
                mini += b
                heapq.heappush(left, -l)
                heapq.heappush(right, r)
                mid = a
            else:
                mini += a - r + b
                heapq.heappush(left, -l)
                heapq.heappush(right, a)
                mid = r
        cnt += 1
for (i, j) in ans:
    print(i, j)
