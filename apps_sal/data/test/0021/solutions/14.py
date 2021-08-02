n = int(input())
ai = list(map(int, input().split()))
mini = 0
maxi = 0
for i in range(n):
    if ai[i] == n:
        maxi = i
    if ai[i] == 1:
        mini = i
print(max(maxi, mini, n - maxi - 1, n - mini - 1))
