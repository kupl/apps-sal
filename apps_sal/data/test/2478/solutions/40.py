n = int(input())
s = input()
cnt_l, cnt_r = 0, 0

for x in s:
    if x == "(":
        cnt_l += 1
    elif cnt_l > 0:
        cnt_l -= 1
    else:
        cnt_r += 1

print((cnt_r * "(" + s + cnt_l * ")"))
