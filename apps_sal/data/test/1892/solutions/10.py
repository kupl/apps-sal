n = int(input())
a = [1]
flag = False
for i in range(n):
    if flag:
        a.append(0)
        flag = False
    else:
        s = 0
        for i in range(len(a)):
            t = a[i]
            a[i] += s
            s += t
            a[i] %= 10**9 + 7
            s %= 10**9 + 7
    if input() == 'f':
        flag = True

print(sum(a) % (10**9 + 7))
