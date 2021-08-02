n = int(input())

inf = 10**9 + 11
arr = []

for i in range(n):
    wh = list(map(int, input().split()))
    wh.sort()
    arr.append(wh)

best_S = inf
cur_S = 0

for h in range(1, 1001):
    cur_S = 0
    for j in range(n):
        if arr[j][0] > h:
            cur_S = inf
            break
        if arr[j][1] <= h:
            cur_S += arr[j][0]
        else:
            cur_S += arr[j][1]
    best_S = min(best_S, cur_S * h)

print(best_S)
