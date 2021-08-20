(a, b) = map(int, input().split())
aa = a
bb = b
ans = 0
ans += min(aa, bb)
print(ans, end=' ')
aa -= ans
bb -= ans
print(max(aa // 2, bb // 2))
