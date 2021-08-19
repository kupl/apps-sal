(x, y, z) = map(int, input().split())
cnt = 0
length = x - 2 * z
cnt += length // (y + z)
length = length % (y + z)
if y <= length:
    cnt += 1
print(cnt)
