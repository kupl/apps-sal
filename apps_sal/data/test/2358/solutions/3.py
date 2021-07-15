s = input()

p_lo = 0
p_hi = len(s) - 1
rem_lo = []
rem_hi = []

while p_lo < p_hi:
    if s[p_lo] == ")":
        p_lo += 1
    elif s[p_hi] == "(":
        p_hi -= 1
    else:
        rem_lo.append(p_lo)
        rem_hi.append(p_hi)
        p_lo += 1
        p_hi -= 1

if len(rem_lo) == 0:
    print(0)
else:
    print(1)
    print(2*len(rem_lo))
    print(*[x + 1 for x in rem_lo + list(reversed(rem_hi))])

