def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


ans = 0
(n, m, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
for i in range(m):
    li = a[0:i] + [-k]
    s = 0
    while True:
        li += a[i + s:min(i + m + s, len(a))]
        li += [-k]
        if i + m + s >= len(a):
            break
        s += m
    ans = max(max_subarray(li) - k, ans)
print(ans)
