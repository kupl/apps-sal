n = int(input())
d, x = map(int, input().split())
li = []
for i in range(n):
    li.append(int(input()))
cnt = 0
for i in li:
    day = 1
    while day <= d:
        day += i
        cnt += 1
print(cnt + x)
