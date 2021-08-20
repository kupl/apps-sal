n = int(input())
a = [0] + list(map(int, input().split()))
b = [0] * (n + 1)
b[-1] = a[-1]
ans = []
for i in range(n, 0, -1):
    cnt = 0
    bi = i
    i += bi
    while i <= n:
        cnt += b[i]
        i += bi
    if cnt % 2 == a[bi]:
        b[bi] = 0
    else:
        b[bi] = 1
        ans.append(bi)
print(len(ans))
if ans:
    print(*ans)
