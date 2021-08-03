def cal():
    s = input()
    num, ans = len(s) - 1, 0
    for i in range(2**num):
        count0, count1 = 0, 0
        for j in range(num):
            count1 += 1
            if (i >> j) & 1:
                ans += int(s[count0:count1])
                count0 = count1
        ans += int(s[count0:count1 + 1])
    print(ans)


cal()
