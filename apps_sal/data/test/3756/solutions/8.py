n, t = map(int, input().split())
x = input()
i = x.find('.')
for j in range(i + 1, n):
    if x[j] > '4':
        for k in range(t):
            j -= 1
            if x[j] != '4': break
        if j == i:
            j -= 1
            while j and x[j] == '9': j -= 1
            x = x[:j] + str(int(x[j]) + 1) + '0' * (i - j - 1)
        else:
            x = x[:j] + str(int(x[j]) + 1)
        break
print(x)
