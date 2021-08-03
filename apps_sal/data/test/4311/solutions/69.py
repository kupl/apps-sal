s = int(input())
line = [0 for i in range(1000001)]
ans = 1
line[s] += 1
while True:
    ans += 1
    if s % 2 == 0:
        s = int(s / 2)
    else:
        s = 3 * s + 1
    line[s] += 1
    if line[s] > 1:
        break
print(ans)
