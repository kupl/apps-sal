S = input()

d1, d2, d3 = 0, 0, 0

if S[0] == 'R':
    d1 = 1
if S[1] == 'R':
    d2 = 1
if S[2] == 'R':
    d3 = 1

print(d2 and (d1 + d2 + d3) or not d2 and (d1 or d3))
