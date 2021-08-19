s = input()
(tmp, ans) = (0, 0)
for i in s:
    if i in {'A', 'C', 'G', 'T'}:
        tmp += 1
    else:
        tmp = 0
    ans = max(ans, tmp)
print(ans)
