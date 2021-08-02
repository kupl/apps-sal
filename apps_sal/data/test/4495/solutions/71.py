a, b, x = map(int, input().split())

cnt = 0
if a % x == 0:
    cnt += 1

# if b % x == 0:
#  cnt += 1

cnt += (b // x - a // x)

print(cnt)
