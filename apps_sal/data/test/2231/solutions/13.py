super_ans = []
for i in range(int(input())):
    n = input()
    if n == '4':
        super_ans.append(input())
        continue
    elif n == '5':
        a = sorted(map(int, input().split()))
        if a[0] == a[1] and a[2] == a[3]:
            super_ans.append(' '.join([str(a[0]), str(a[0]), str(a[2]), str(a[2])]))
        elif a[0] == a[1] and a[3] == a[4]:
            super_ans.append(' '.join([str(a[0]), str(a[0]), str(a[3]), str(a[3])]))
        else:
            super_ans.append(' '.join([str(a[-1]), str(a[-1]), str(a[-3]), str(a[-3])]))
        continue
    d = 10 ** 9
    ans = []
    t = tc = x = y = 0
    for ai in sorted(map(int, input().split())):
        if t == ai:
            tc += 1
            if tc == 2:
                x = y
                y = ai
                if x and y / x < d:
                    d = y / x
                    ans = [x, y]
            elif tc == 4:
                ans = [t, t]
                break
        else:
            t = ai
            tc = 1
    super_ans.append(' '.join(map(str, ans * 2)))
print('\n'.join(super_ans))
