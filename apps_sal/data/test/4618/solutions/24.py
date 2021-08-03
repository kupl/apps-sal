import collections

s = input()
k = int(input())
b = collections.Counter(s)
c = sorted(b.items())
con = []
n = 0
while True:
    con.append(c[n][0])
    if len(con) == k:
        break
    for i in range(len(c)):
        check = c[n][0] + c[i][0]
        if check in s:
            con.append(check)
            if len(con) >= k:
                break
            for i_2 in range(len(c)):
                check_2 = check + c[i_2][0]
                if check_2 in s:
                    con.append(check_2)
                    if len(con) >= k:
                        break
                    for i_3 in range(len(c)):
                        check_3 = check_2 + c[i_3][0]
                        if check_3 in s:
                            con.append(check_3)
                            if len(con) >= k:
                                break
                            for i_4 in range(len(c)):
                                check_4 = check_3 + c[i_4][0]
                                if check_4 in s:
                                    con.append(check_4)
                                    if len(con) >= k:
                                        break
    if len(con) >= k:
        break
    n += 1
print(con[k - 1])
