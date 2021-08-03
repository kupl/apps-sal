T = int(input())
for i in range(T):
    s = list(input())
    s.sort()
    k = len(s)
    s1 = []
    s3 = []
    s2 = [0] * 150
    pro = True
    for j in range(k):
        s2[ord(s[j])] += 1
    for j in range(97, 123, 2):
        if s2[j] > 0:
            s3 += [chr(j)] * s2[j]
    for j in range(98, 123, 2):
        if s2[j] > 0:
            s3 += [chr(j)] * s2[j]
    for j in range(98, 123, 2):
        if s2[j] > 0:
            s1 += [chr(j)] * s2[j]
    for j in range(97, 123, 2):
        if s2[j] > 0:
            s1 += [chr(j)] * s2[j]
    for j in range(k - 1):
        if abs(ord(s1[j]) - ord(s1[j + 1])) == 1:
            pro = False
            break
    if pro:
        print(*s1, sep="")
    else:
        pro = True
        for j in range(k - 1):
            if abs(ord(s3[j]) - ord(s3[j + 1])) == 1:
                pro = False
        if pro:
            print(*s3, sep="")
        else:
            print("No answer")
