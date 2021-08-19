# 問題：https://atcoder.jp/contests/abc146/tasks/abc146_a

week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
s = input()
for i, day in enumerate(week):
    if day == s:
        res = 7 - i
        break
res = 7 - i
print(res)
