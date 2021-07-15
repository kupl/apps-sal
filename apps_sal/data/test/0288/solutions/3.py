n = int(input())
prev, cur = 1, 2
iters = 0
while (cur < n):
    prev, cur = cur, cur + prev
    iters += 1
ans = iters + bool(cur == n)
print(ans)
