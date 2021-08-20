s = list(map(int, input().split()))
a = int(s[0])
b = int(s[1])
x = int(s[2])
y = int(s[3])
move_withoutstep_1 = 9999999999
move_withoutstep_2 = 9999999999
if a > b:
    move_withoutstep_1 = (a - b - 1) * x + (a - b) * x
elif a <= b:
    move_withoutstep_2 = (b - a + 1) * x + (b - a) * x
move_upstairs = 9999999999
move_downstairs = 9999999999
if a < b:
    move_upstairs = (b - a) * y + x
elif a > b:
    move_downstairs = (a - b - 1) * y + x
print(min(move_withoutstep_1, move_withoutstep_2, move_upstairs, move_downstairs))
