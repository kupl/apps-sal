N = int(input())
src = [tuple(map(int, input().split())) for i in range(N)]
ans = 1
pa = pb = 0
for a, b in src:
    if pa == pb:
        ans += min(a, b) - pa
    elif pa < pb:
        if min(a, b) >= pb:
            ans += min(a, b) - pb + 1
    else:
        if min(a, b) >= pa:
            ans += min(a, b) - pa + 1
    pa, pb = a, b
print(ans)
