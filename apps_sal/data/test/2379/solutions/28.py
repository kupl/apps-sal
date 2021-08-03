n, k, c = [int(i) for i in input().split()]
s = input()

work1 = [0] * k
work2 = [0] * k
cnt = 0
day = 0

while cnt < k:
    if s[day] == 'o':
        work1[cnt] = day
        cnt += 1
        day += (c + 1)
    else:
        day += 1


cnt = k - 1
day = n - 1

while cnt >= 0:
    if s[day] == 'o':
        work2[cnt] = day
        cnt -= 1
        day -= (c + 1)
    else:
        day -= 1


for i in range(k):
    if work1[i] == work2[i]:
        print((work1[i] + 1))
