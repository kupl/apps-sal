t = int(input())
for loop in range(t):
    n = int(input())
    s = input()
    lis = []
    for k in range(1, n + 1):
        temp = list(s[:k - 1])
        if (n - k + 1) % 2 == 1:
            temp.reverse()
        ns = s[k - 1:] + ''.join(temp)
        lis.append([ns, k])
    lis.sort()
    print(lis[0][0])
    print(lis[0][1])
