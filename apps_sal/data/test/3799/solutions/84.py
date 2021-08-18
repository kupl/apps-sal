s = input()
count = 0
player = ['First', 'Second']

ans = 0
while ans == 0:
    if len(s) == 2:
        ans = player[(count + 1) % 2]
    else:
        for i in range(1, len(s) - 1):
            if s[i - 1] != s[i + 1]:
                s = s[:i] + s[i + 1:]
                break
        else:
            ans = player[(count + 1) % 2]
    count += 1
print(ans)
