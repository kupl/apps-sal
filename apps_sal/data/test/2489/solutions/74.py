import bisect
N = int(input())
A = [int(x) for x in input().split()]
A = sorted(A)
maxA = max(A)
ans = 0
so_list = [1] * (maxA + 1)
index = 0
i = 0
while i < N:
    flag = 0
    now = A[i]
    if so_list[now] == 1:
        index = 0
        flag = 1
        while index + now <= maxA:
            so_list[index + now] = 0
            index += now
    right = bisect.bisect_right(A, now)
    if right - i == 1:
        if flag == 1:
            ans += 1
        i = right
    else:
        i += 1
print(ans)
