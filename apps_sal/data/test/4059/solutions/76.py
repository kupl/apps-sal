n = int(input())
cnt = 0
for a in range(1, n):
    b = (n - 1) // a
    cnt += b
print(cnt, flush=True)
