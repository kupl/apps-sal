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

    t = tc = x = y = a1 = a2 = 0

    for ai in sorted(map(int, input().split())):
        if t == ai:
            tc += 1

            if tc == 2:
                x = y
                y = ai

                if x and y / x < d:
                    d = y / x
                    a1, a2 = x, y

            elif tc == 4:
                a1 = a2 = t
                break
        else:
            t = ai
            tc = 1

    super_ans.append(' '.join([str(a1), str(a1), str(a2), str(a2)]))

print('\n'.join(super_ans))
