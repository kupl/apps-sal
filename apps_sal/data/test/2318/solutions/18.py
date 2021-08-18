n = int(input())
for tee in range(n):
    s = input()
    t = input()
    if len(s) > len(t):
        print("NO")
        continue
    if len(s) == len(t):
        if s == t:
            print("YES")
        else:
            print("NO")
        continue
    arr = []
    i = 0
    pre = None
    cc = 0
    while i < len(s):
        if pre == None:
            pre = s[i]
            cc = 1
        else:
            if pre == s[i]:
                cc += 1
            else:
                arr.append([pre, cc])
                pre = s[i]
                cc = 1
        i += 1
    arr.append([pre, cc])
    brr = []
    i = 0
    pre = None
    cc = 0
    while i < len(t):
        if pre == None:
            pre = t[i]
            cc = 1
        else:
            if pre == t[i]:
                cc += 1
            else:
                brr.append([pre, cc])
                pre = t[i]
                cc = 1
        i += 1
    brr.append([pre, cc])
    if len(brr) != len(arr):
        print("NO")
    else:
        check = True
        for i in range(len(arr)):
            if arr[i][0] != brr[i][0] or arr[i][1] > brr[i][1]:
                check = False
                break
        if not check:
            print("NO")
        else:
            print("YES")
