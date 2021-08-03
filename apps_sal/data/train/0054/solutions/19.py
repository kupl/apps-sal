from sys import stdin
q = int(stdin.readline().strip())
for i in range(q):
    n = int(stdin.readline().strip())
    s = list(map(int, stdin.readline().strip().split()))
    flag = False
    for j in range(12):

        x = 2**j

        s1 = []
        cnt = 0
        for k in range(len(s)):
            if s[k] == x:
                cnt += 1
            else:
                s1.append(s[k])
            if s[k] == 2048:
                flag = True
        y = cnt // 2
        s1 = s1 + [x * 2] * y
        s = s1.copy()
    if flag:
        print("YES")
    else:
        print("NO")
