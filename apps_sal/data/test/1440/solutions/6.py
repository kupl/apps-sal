import sys

n = int(sys.stdin.readline().strip())
s = list(map(int, sys.stdin.readline().strip().split()))
t = 0
i = 0
j2 = 0
while i < n:
    x = s[i] // 3
    t = t + x
    s[i] = s[i] - 3 * x
    if s[i] != 0:
        j = max([i + 1, j2])
        while j < n:
            j2 = j
            if s[j] >= 2:
                t = t + 1
                s[j] = s[j] - 2
                s[i] = s[i] - 1
                if s[i] == 0:
                    j = n
            else:
                j = j + 1
    if s[i] != 0:
        i = n
    else:
        i = i + 1

print(t)
