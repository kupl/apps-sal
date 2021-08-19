(a, b) = map(int, input().split())
cnt = 0
while a > 0 and b > 0 and (b > 1 or a > 1):
    if a < b:
        a += 1
        b -= 2
    else:
        a -= 2
        b += 1
    cnt += 1
print(cnt)
