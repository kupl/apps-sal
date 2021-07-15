x = int(input())

cnt = 0
s = 0

for i in range(1, x+1):
    cnt += 1
    s += i
    if s >= x:
        break

print(cnt)
