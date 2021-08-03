n = int(input())
s = input()
a = [0] * 10
for i in s:
    if i == 'L':
        for j in range(10):
            if a[j] == 0:
                a[j] = 1
                break
    elif i == 'R':
        for j in range(10):
            if a[-j - 1] == 0:
                a[-j - 1] = 1
                break
    else:
        k = int(i)
        a[k] = 0
for i in range(10):
    print(a[i], end="")
