N, M = map(int, input().split())
store_m = [list(map(int, input().split())) for i in range(N)]
store = sorted(store_m)
buy = 0
cost = 0
for i in range(N):
    buy += store[i][1]
    if buy < M:
        cost += store[i][0] * store[i][1]
    else:
        cost += store[i][0] * (M - (buy - store[i][1]))
        print(cost)
        return
