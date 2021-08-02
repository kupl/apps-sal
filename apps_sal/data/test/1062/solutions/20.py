n = int(input())
s = input()
t = input()
dis = 0
d = [[False for i in range(30)] for i in range(30)]
x = [[0 for i in range(30)] for i in range(30)]
for i in range(n):
    if s[i] != t[i]:
        dis += 1
        d[ord(s[i]) - ord('a')][ord(t[i]) - ord('a')] = True
        x[ord(s[i]) - ord('a')][ord(t[i]) - ord('a')] = i + 1


def progress():
    for i in range(26):
        for j in range(26):
            if (d[i][j]) and (d[j][i]):
                print("{}\n{} {}".format(dis - 2, x[i][j], x[j][i]))
                return 0
    for i in range(26):
        for j in range(26):
            if d[i][j]:
                for t in range(26):
                    if d[j][t]:
                        print("{}\n{} {}".format(dis - 1, x[i][j], x[j][t]))
                        return 0
    print("{}\n{} {}".format(dis, -1, -1))


progress()
