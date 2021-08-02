t = int(input())
for _ in range(t):
    s = input()
    m = int(input())
    b = list(map(int, input().split()))
    slist = []
    for i in range(len(s)):
        slist.append(s[i])
    slist.sort()
    slist.reverse()
    slist2 = []
    slist2.append([slist[0], 1])
    for i in range(1, len(s)):
        if slist2[-1][0] == slist[i]:
            slist2[-1][1] += 1
        else:
            slist2.append([slist[i], 1])
    pointer = 0
    done = [0] * m
    ans = [0] * m
    while sum(done) < m:
        zeros = []
        for i in range(m):
            if b[i] == 0 and done[i] == 0:
                zeros.append(i)
        num = len(zeros)
        while slist2[pointer][1] < num:
            pointer += 1
        for i in zeros:
            done[i] = 1
            ans[i] = slist2[pointer][0]
            for j in range(m):
                b[j] -= abs(i - j)
        pointer += 1
    print(''.join(ans))
