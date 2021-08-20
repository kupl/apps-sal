import heapq
Q = int(input())
(A_left, A_right) = ([], [])
(A_left_sum, A_right_sum) = (0, 0)
heapq.heapify(A_left)
heapq.heapify(A_right)
B_sum = 0
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        now = query[1]
        B_sum += query[2]
        (l, r) = (len(A_left), len(A_right))
        if l <= r:
            heapq.heappush(A_right, now)
            A_right_sum += now
            out = heapq.heappop(A_right)
            A_right_sum -= out
            heapq.heappush(A_left, -out)
            A_left_sum += out
        else:
            heapq.heappush(A_left, -now)
            A_left_sum += now
            out = -heapq.heappop(A_left)
            A_left_sum -= out
            heapq.heappush(A_right, out)
            A_right_sum += out
    else:
        m = -A_left[0]
        ans = len(A_left) * m - A_left_sum - len(A_right) * m + A_right_sum + B_sum
        print('{0} {1}'.format(m, ans))
