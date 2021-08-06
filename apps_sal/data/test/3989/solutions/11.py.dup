from collections import *
ans = [1, 6, 8, 9]
rem = []
al = defaultdict(int)
for i in range(len(ans)):
    for j in range(len(ans)):
        for m in range(len(ans)):
            for t in range(len(ans)):
                re = [i, j, m, t]
                if(len(set(re)) == 4):
                    q = pow(10, 3) * ans[i] + (pow(10, 2) * ans[j]) + (pow(10, 1) * ans[m]) + (ans[t])
                    if(al[q % 7] == 0):

                        rem.append([q % 7, q])

                        al[q % 7] = 1

s = input()
rem.sort()
ans = []
for i in range(len(s)):
    ans.append(int(s[i]))
count = 0
ans.remove(1)
ans.remove(6)
ans.remove(8)
ans.remove(9)
i = 0

while(i < len(ans)):

    if(i == 0):
        while(i < len(ans) and ans[i] == 0):
            count += 1
            i += 1
        i += 1
    else:
        i += 1
temp = []
for i in range(count, len(ans)):
    temp.append(ans[i])
fin = 0
if(len(temp) == 0):
    s = str(rem[0][1]) + '0' * count
    print(s)
    return
else:
    for i in range(len(temp)):
        fin = fin + (pow(10, len(temp) - i - 1, 7) * (temp[i] % 7) % 7)
        fin %= 7

    if(fin == 0):
        m = ''.join(map(str, temp)) + str(rem[fin][1]) + ('0' * count)
    if(fin == 1):
        m = ''.join(map(str, temp)) + str(rem[3][1]) + ('0' * count)
    if(fin == 2):
        m = ''.join(map(str, temp)) + str(rem[6][1]) + ('0' * count)

    if(fin == 3):
        m = ''.join(map(str, temp)) + str(rem[2][1]) + ('0' * count)
    if(fin == 4):
        m = ''.join(map(str, temp)) + str(rem[5][1]) + ('0' * count)
    if(fin == 5):
        m = ''.join(map(str, temp)) + str(rem[1][1]) + ('0' * count)
    if(fin == 6):
        m = ''.join(map(str, temp)) + str(rem[4][1]) + ('0' * count)

    print(m)
