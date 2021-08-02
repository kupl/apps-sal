def judge(ss):
    n = len(ss)
    for i in range(n):
        if((int(ss[i]) % 2 == 0)):  # input() haoxiang doushi str
            return i
    return -1


s = input()
p = judge(s)
# print(p)
if(p == -1):
    print("-1")
else:
    n = len(s)
    flag = 0
    las = n - 1
    for i in range(n):
        if(int(s[i]) % 2 == 0):
            p = i
            if int(s[i]) < int(s[las]):
                temp = s[0:i] + s[las] + s[i + 1:n - 1] + s[i]
                print(temp)
                flag = 1
                break;

    if not flag:
        temp = s[0:p] + s[las] + s[p + 1:n - 1] + s[p]
        print(temp)
