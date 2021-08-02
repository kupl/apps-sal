T = int(input())
for i in range(T):
    X = int(input())
    Y = input()
    ans = 0
    count = 0
    start = False
    for j in range(len(Y)):
        if Y[j] == 'A':
            start = True
            ans = max(ans, count)
            count = 0

        else:
            if start:
                count += 1
    ans = max(ans, count)
    print(ans)
