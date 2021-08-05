S = input()

flag = 1
c_count = 0
ans = 'AC'
if S[0] != 'A':
    ans = 'WA'
for i in range(1, len(S)):
    if (i == 1 or i == len(S) - 1) and S[i].islower() == False:
        ans = 'WA'
    elif 2 <= i <= len(S) - 2:
        if S[i] == 'C':
            c_count += 1
if c_count != 1:
    ans = 'WA'
print(ans)
