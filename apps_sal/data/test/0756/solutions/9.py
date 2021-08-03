n = int(input())
ti = list(map(int, input().split()))
t2 = [0] * 91
for i in ti:
    t2[i] = 1
num = 0
ans = 0
for i in range(1, 91):
    if t2[i] == 0:
        num += 1
    else:
        num = 0
    ans = i
    if num >= 15:
        break
print(ans)
