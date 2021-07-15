n = int(input())
cur = 1
ans = []
while n > cur:
    n -= cur
    ans.append(cur)
    cur += 1
if n < cur:
    ans[-1] += n
else:
    ans.append(n)
print(len(ans))
print(*ans)

