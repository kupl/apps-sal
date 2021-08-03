t = int(input())
for i in range(t):
    n, k, d = list(map(int, input().split()))
    L = list(map(int, input().split()))
    Balance = [0] * k
    Is = 0
    for i in range(d):
        Balance[L[i] - 1] += 1
        if Balance[L[i] - 1] == 1:
            Is += 1
    minIs = Is
    for i in range(d, n):
        Balance[L[i - d] - 1] -= 1
        if Balance[L[i - d] - 1] == 0:
            Is -= 1
        Balance[L[i] - 1] += 1
        if Balance[L[i] - 1] == 1:
            Is += 1
        if Is < minIs:
            minIs = Is
    print(minIs)
