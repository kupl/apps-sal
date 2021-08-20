n = int(input())
s = input()
t = input()
s_1 = 0
t_1 = 0
for i in range(2 * n):
    if s[i] == '1':
        s_1 += 1
    if t[i] == '1':
        t_1 += 1
first = 0
second = 0
r = 0
for i in range(2 * n):
    if s[i] == '1' and t[i] == '0':
        first += 1
    elif s[i] == '0' and t[i] == '1':
        second += 1
    elif s[i] == '1' and t[i] == '1':
        r += 1
if r % 2 == 1:
    first += 1
if s_1 > t_1:
    print('First')
elif first == second or first == second - 1:
    print('Draw')
elif first > second:
    print('First')
elif first < second:
    print('Second')
