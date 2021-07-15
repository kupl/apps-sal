m = int(input())
curr = 5
power = 1
while power < m:
    curr += 5
    s = curr
    while s % 5 == 0:
        s //= 5
        power += 1
if power > m:
    print(0)
else:
    print(5)
    for i in range(curr, curr + 5):
        print(i, end=' ')
