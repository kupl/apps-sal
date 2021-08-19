(a, b) = list(map(int, input().split()))
cnt = 0
num = 1
while num < b:
    num += a - 1
    cnt += 1
print(cnt)
