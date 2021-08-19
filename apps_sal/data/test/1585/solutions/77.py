x, y = map(int, input().split())
cnt = 1
while x * 2 <= y:
    # print(x*2)
    cnt += 1
    x = x * 2
print(cnt)
