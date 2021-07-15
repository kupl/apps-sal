for __ in range(int(input())):
    n, s = list(map(int, input().split()))
    ar = list(map(int, input().split()))
    if sum(ar) <= s:
        print(0)
    else:
        ans = 0
        lol = ar[0]
        kek = 0
        ans1 = 0
        flag = 0
        for i in range(n):
            if ar[i] > lol and  flag == 0:
                lol = ar[i]
                kek = i
            if s - ar[i] >= 0 and flag == 0:
                ans += 1
                s -= ar[i]
            elif s - ar[i] >= 0:
                ans1 += 1
                s -= ar[i]
            elif flag == 1:
                break
            else:
                ans1 = ans - 1
                s += lol
                flag = 1
                if s - ar[i] >= 0:
                    ans1 += 1
                    s -= ar[i]
                else:
                    break
        print(kek + 1)
