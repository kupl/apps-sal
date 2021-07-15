n = int(input())
home = list(map(int, input().split()))
suff = [0] * n
for i in range(n - 2, -1, -1):
    suff[i] = max(suff[i + 1], home[i + 1])
for i in range(n):
    if home[i] > suff[i]:
        print(0, end=" ")
    else:
        print(suff[i] - home[i] + 1, end=" ")

