[e1, e2] = map(int, input().split(':'))
[s1, s2] = map(int, input().split(':'))

total1 = e1 * 60 + e2
total2 = s1 * 60 + s2
ans = 0
if total1 >= total2:
    ans = total1 - total2
else:
    ans = 1440 - total2 + total1
print('{:02}:{:02}'.format(int(ans / 60), int(ans % 60)))
