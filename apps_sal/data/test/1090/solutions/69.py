n,k = map(int,input().split())
s = input()

from_start = 0
RtoL = 0
LtoR = 0
for i in range(n-1):
    if s[i] == s[i+1]:
        from_start += 1
    elif s[i] == 'R' and s[i+1] == 'L':
        RtoL += 1
    elif s[i] == 'L' and s[i+1] == 'R':
        LtoR += 1
add = 0
while (RtoL or LtoR) and k:
    k-=1
    if RtoL and LtoR:
        add += 2
        RtoL -= 1
        LtoR -= 1
    elif RtoL:
        add += 1
        RtoL -= 1
    elif LtoR:
        add += 1
        LtoR -= 1
print(from_start+add)
