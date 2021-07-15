s = input()
a_count = 0
dp1 = 0     # last letter is 'b'
dp2 = 0     # last letter is 'a'
for i in range(len(s)):
    if(s[i]=='a'):
        a_count += 1
        dp2 = max(dp1,dp2)+1
    else:
        dp1 = max(a_count,dp1)+1
print(max(dp1,dp2))
