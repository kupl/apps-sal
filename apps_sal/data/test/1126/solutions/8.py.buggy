N, X, M = list(map(int, input().split()))

A = [X]
item = set()
for i in range(N - 1):
    next = (A[i] ** 2) % M
    if next in item:
        loop_start = A.index(next)
        loop_length = len(A) - loop_start
        loop_times = (N - loop_start) // loop_length
        loop_remain = (N - loop_start) % loop_length
        cnt = sum(A[:loop_start]) + (sum(A[loop_start:]) * loop_times) + sum(A[loop_start:loop_start + loop_remain])
        print(cnt)
        return
    A.append(next)
    item.add(next)
print((sum(A)))
