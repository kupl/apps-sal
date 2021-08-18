n = int(input())
x = input()
y = input()

now = 1
flag = 0


i = 0
while (i < n):
    if (i == 0):
        if (x[i] == y[i]):
            now *= 3
            flag = 1
            i += 1
        else:
            now *= 6
            flag = 0
            i += 2
    else:
        if (x[i] == y[i]):
            if (flag == 0):
                flag = 1
                i += 1
            else:
                now *= 2
                now = now % 1000000007
                flag = 1
                i += 1
        else:
            if (flag == 0):
                now *= 3
                now = now % 1000000007
                i += 2
                flag = 0
            else:
                now *= 2
                now = now % 1000000007
                i += 2
                flag = 0

print(now)
