n = input()
cnt = 0
S = input()
m = 0
for s in S:
    if s == "(":
        cnt += 1
    else:
        cnt -= 1
    m = min(m, cnt)

left = -min(0, m)
right = abs(cnt - m)
print(("(" * left + S + ")" * right))

