s = input()
if len(s) == 2:
    if s[0] == s[1]:
        print(1, 2)
    else:
        print(-1, -1)
else:
    for i in range(len(s) - 2):
        temp = {}
        for j in range(3):
            temp.setdefault(s[i + j], 0)
            temp[s[i + j]] += 1
        if max(temp.values()) >= 2:
            print(i + 1, i + 3)
            break
    else:
        print(-1, -1)
