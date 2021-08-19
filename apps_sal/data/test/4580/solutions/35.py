n = int(input())
a = list(map(int, input().split()))

rate = [0] * 9
over = 0

for i in a:
    for j in range(1, 9):
        if 400 * (j - 1) <= i < 400 * j:
            rate[j] = 1
            break
        elif i >= 3200:
            over += 1
            break

ansmin = rate.count(1)
ansmax = rate.count(1)
if ansmin == 0:
    ansmin = 1

if over > 0:
    ansmax += over

# print(rate,over)
print(ansmin, ansmax)
