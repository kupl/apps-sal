t = int(input())
for i in range(0, t):
    str = input()
    answer = []
    p = [1, 2, 3, 4, 6, 12]
    for j in range(0, len(p)):
        (d1, d2) = (p[j], 12 // p[j])
        cnt = [0 for h in range(0, d2)]
        for i2 in range(0, 12):
            tt = i2 % d2
            cnt[tt] += str[i2] == 'X'
        ans_cand = False
        for i2 in range(0, d2):
            if cnt[i2] == d1:
                ans_cand = True
        if ans_cand:
            answer.append('%dx%d' % (d1, d2))
    print(len(answer), end=' ')
    for j in range(0, len(answer)):
        print(answer[j], end=' ')
    print()
