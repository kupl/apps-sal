(n, k) = list(map(int, input().split()))
ans = 0
num_multiple = n // k
ans += num_multiple ** 3
if k % 2 == 0:
    num_multiple = (n + k // 2) // k
    ans += num_multiple ** 3
print(ans)
