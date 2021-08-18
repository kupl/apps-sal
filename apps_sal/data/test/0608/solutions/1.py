s = input()
if s.isnumeric():
    k = int(s)
    if k >= 3 and k <= 1000:
        s = input().split(' ')
        gifts = 0
        i = 0
        while i < len(s):
            if (i == len(s) - 2) or (i == len(s) - 1):
                break
            if s[i].isnumeric():
                t = int(s[i])
                if (t >= 1) and (t <= 5):
                    if ((s[i] == '4') or (s[i] == '5')) and ((s[i + 1] == '4') or (s[i + 1] == '5')) and ((s[i + 2] == '4') or (s[i + 2] == '5')):
                        gifts += 1
                        i += 2
            i += 1
        print(gifts)
