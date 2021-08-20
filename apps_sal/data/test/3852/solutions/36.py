N = int(input())
A = list(map(int, input().split()))
p = 0
m = 0
for i in range(N):
    if A[i] >= 0:
        p += 1
    else:
        m += 1
ans = []
if m == 0:
    for i in range(N - 1):
        ans.append((i + 1, i + 2))
    print(len(ans))
    for (x, y) in ans:
        print(x, y)
elif p == 0:
    for i in range(N - 1, 0, -1):
        ans.append((i + 1, i))
    print(len(ans))
    for (x, y) in ans:
        print(x, y)
else:
    big = -1 * float('inf')
    big_idx = 0
    small = float('inf')
    small_idx = 0
    for i in range(N):
        if big < A[i]:
            big = A[i]
            big_idx = i
        if small > A[i]:
            small = A[i]
            small_idx = i
    if abs(big) >= abs(small):
        for i in range(N):
            if A[i] < 0:
                ans.append((big_idx + 1, i + 1))
        for i in range(N - 1):
            ans.append((i + 1, i + 2))
        print(len(ans))
        for (x, y) in ans:
            print(x, y)
    else:
        for i in range(N):
            if A[i] > 0:
                ans.append((small_idx + 1, i + 1))
        for i in range(N - 1, 0, -1):
            ans.append((i + 1, i))
        print(len(ans))
        for (x, y) in ans:
            print(x, y)
