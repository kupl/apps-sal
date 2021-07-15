x = int(input())
now = 100
cnt = 0
while now < x:
    now += now//100
    cnt += 1
print(cnt)
