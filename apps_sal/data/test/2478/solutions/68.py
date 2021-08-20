n = int(input())
s = input()
ans = s
while s.count('()') > 0:
    s = s.replace('()', '')
cnt_l = s.count(')')
cnt_r = s.count('(')
print(cnt_l * '(' + ans + cnt_r * ')')
