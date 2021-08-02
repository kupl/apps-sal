s = input()
abc = [0] * 26
cnt1 = 0;
ans = 1;
for i in range(len(s)):
    if s[i] == '?':
        if i == 0:
            ans *= 9
        else:
            ans *= 10
    elif (s[i] >= 'A') and (s[i] <= 'Z'):
        if abc[(ord(s[i]) - ord('A'))] == 0:
            if i == 0:
                abc[(ord(s[i]) - ord('A'))] = 1
                ans *= 9
                cnt1 += 1
            else:
                abc[(ord(s[i]) - ord('A'))] = 1
                ans *= (10 - cnt1)
                cnt1 += 1
print(ans)
