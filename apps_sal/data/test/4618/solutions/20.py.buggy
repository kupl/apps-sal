import sys
s = input()
K = int(input())

a_list = sorted(set(s))
for i in a_list:
    if K == 1:
        print(i)
        return
    p = []
    for j, x in enumerate(s):
        if x == i:
            p.append(s[j:min(j + K, len(s))])
    p.sort()
    t = K
    for j in range(len(p)):
        if j != len(p) - 1:
            if p[j] == p[j + 1][0:len(p[j])]:
                continue
        if len(p[j]) < t:
            t -= len(p[j]) - 1
        else:
            print(p[j][0:t])
            return
    K = t - 1
