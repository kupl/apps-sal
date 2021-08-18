from sys import stdin, stdout


def ri():
    return list(map(int, input().split()))


n = int(input())

s = []
for i in range(n):
    s.append(stdin.readline().strip())

for i in range(n - 1, 0, -1):
    mind = min(len(s[i]), len(s[i - 1]))
    for j in range(mind):
        if s[i - 1][j] < s[i][j]:
            break
        elif s[i - 1][j] == s[i][j]:
            if j + 1 == mind:
                s[i - 1] = s[i - 1][:mind]
                break
            continue
        else:
            s[i - 1] = s[i - 1][:j]
            break
print('\n'.join(s))
