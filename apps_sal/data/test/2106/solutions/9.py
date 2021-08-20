from math import ceil
X = list(map(int, input().split()))
Distance = list(map(int, input().split()))
Fuel = list(map(int, input().split()))
(Tank, Time, Max) = (0, 0, 0)
for i in range(X[0]):
    Tank += Fuel[i]
    Max = max(Max, Fuel[i])
    Stay = max(0, ceil((Distance[i] - Tank) / Max))
    Time += Stay * X[1] + Distance[i]
    Tank += Stay * Max - Distance[i]
print(Time)
