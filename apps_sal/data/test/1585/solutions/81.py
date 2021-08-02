x, y = list(map(int, input().split()))
num = x
cnt = 0
while(num <= y):
    num *= 2
    cnt += 1
print(cnt)
