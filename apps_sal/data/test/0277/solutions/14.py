(a, b, c) = map(int, input().split(' '))
pwr = 0
while a != 1:
    pwr += 1
    a = a // 2
ans = 1
for j in range(1, pwr):
    if (b - 1) // 2 ** j != (c - 1) // 2 ** j:
        ans += 1
if ans == pwr:
    print('Final!')
else:
    print(ans)
