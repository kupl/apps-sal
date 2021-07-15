from bisect import bisect_left
N = int(input())
L_list = list(map(int, input().split()))
L_list.sort()

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        a, b = L_list[i], L_list[j]
        r = bisect_left(L_list, a+b)
        ans += max(0,r-j-1)
print(ans)

