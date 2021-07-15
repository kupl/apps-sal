s = input()

ans = 6

for i in range (0, 10):
    for j in range (0, 10):
        for k in range(0, 10):
            for f in range (0, 10):
                for f1 in range(0, 10):
                    for f2 in range(0, 10):
                        if(i + j + k == f + f1 + f2):
                            cnt = 0
                            if i != (ord(s[0]) - ord('0')):
                                cnt = cnt + 1
                            if j != (ord(s[1]) - ord('0')):
                                cnt = cnt + 1
                            if k != (ord(s[2]) - ord('0')):
                                cnt = cnt + 1
                            if f != (ord(s[3]) - ord('0')):
                                cnt = cnt + 1
                            if f1 != (ord(s[4]) - ord('0')):
                                cnt = cnt + 1
                            if f2 != (ord(s[5]) - ord('0')):
                                cnt = cnt + 1
                        ans = min(ans, cnt)
print(ans)
