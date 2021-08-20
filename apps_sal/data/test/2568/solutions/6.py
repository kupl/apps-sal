tt = int(input())
for loop in range(tt):
    s = input()
    lis = [-1]
    for i in s:
        if i == '-':
            lis.append(lis[-1] + 1)
        else:
            lis.append(lis[-1] - 1)
    now = -1
    ans = 0
    for i in range(1, len(lis)):
        if lis[i] > now:
            ans += i * (lis[i] - now)
            now = lis[i]
    print(ans + len(s))
