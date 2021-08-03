
a, b = map(int, input().split())
cnt = 0
cnt += a
if b < a:
    cnt -= 1
print(cnt)
