n = int(input())
s = input()
for ln in range(1, n):
    for i in range(n):
        if i + ln * 4 < n:
            if s[i] == s[i + ln] == s[i + ln * 2] == s[i + ln * 3] == s[i + ln * 4] == '*':
                print('yes')
                return
print('no')
