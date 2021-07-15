s = input()
if len(s) == 1:
    print(0)
else:
    cnt = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            cnt += 1

    print(cnt)
