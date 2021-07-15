def longest(n,k,a):
    f = [0] * 1000001
    d = 0
    r = 0
    l = 0
    ans_l = 0
    ans_r = 0
    for r in range(0, n):
        f[a[r]] += 1
        if f[a[r]] == 1:
            d +=1
        while d > k:
            f[a[l]] -= 1
            if f[a[l]] == 0:
                d -= 1
            l += 1
        if ans_r - ans_l < r - l:
            ans_r = r
            ans_l = l
    return str(ans_l + 1) + " "+ str(ans_r + 1)
line_1 = list(map(int, input().split()))
n = line_1[0]
k = line_1[1]
line_2 = list(map(int, input().split()))

print(longest(n, k, line_2))
"""
5 5
1 2 3 4 5
"""
"""
9 3
6 5 1 2 3 2 1 4 5
"""
"""
3 1
1 2 3
"""

