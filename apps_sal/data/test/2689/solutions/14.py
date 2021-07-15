s = input()
new_s = ''
for i in s:
    if i.isalpha():
        new_s += i

if new_s == new_s[::-1]:
    print('Return')
else:
    print('Continue')
