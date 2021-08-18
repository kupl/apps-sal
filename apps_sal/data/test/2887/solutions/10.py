t = 1
for t_cases in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    t = list(map(int, input().split()))
    for i in range(0, n):
        temp = 0
        for j in range(0, i + 1):
            if(v[j] >= t[i]):
                temp += t[i]
            else:
                temp += v[j]
            v[j] = max(0, v[j] - t[i])
        print(temp, end=' ')
