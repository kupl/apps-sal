h = int(input())

cnt = 0
ans = 0

while h > 1:
    h = h // 2
    cnt += 1
    ans += 2**cnt

print(ans + 1)
