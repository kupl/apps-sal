q = int(input())
for _ in range(q):
    n = int(input())
    s = [input() for i in range(n)]
    cnt1 = 0
    cnt0 = 0
    cnt_odd = 0
    for i in range(n):
        if len(s[i]) % 2 == 1:
            cnt_odd += 1
        for j in range(len(s[i])):
            if s[i][j] == "1":
                cnt1 += 1
            else:
                cnt0 += 1
    
    if cnt_odd == 0:
        if cnt0 % 2 == 1 and cnt1 % 2 == 1:
            print(n-1)
        else:
            print(n)
    else:
        print(n)
