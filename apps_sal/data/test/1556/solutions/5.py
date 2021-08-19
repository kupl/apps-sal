import heapq

n, k, X = list(map(int, input().split()))
a = list(map(int, input().split()))
Q = []
sit = 0

for i, x in enumerate(a):
    if x < 0:
        sit += 1
    heapq.heappush(Q, (abs(x), x, i))

sit = sit % 2

while k > 0:
    (val, x, i) = heapq.heappop(Q)
    change = None

    if x < 0:
        if sit == 1:
            change = x - X
        else:
            change = x + X
    else:
        if sit == 1:
            change = x + X
        else:
            change = x - X

    if (x * change < 0) or (x < 0 and change == 0) or (x == 0 and change < 0):
        sit = (sit + 1) % 2

    heapq.heappush(Q, (abs(change), change, i))
    k -= 1

ans = [0] * n
for (val, x, i) in Q:
    ans[i] = str(x)
print(' '.join(ans))

# 5 3 1
# 5 4 3 5 2

# 5 3 1
# 5 4 3 5 5

# 5 3 1
# 5 4 4 5 5

# 3 2 7
# 5 4 2
