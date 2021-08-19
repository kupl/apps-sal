N = int(input())
(T, A) = map(int, input().split())
H = list(map(int, input().split()))
mini = float('inf')
res = 0
for i in range(len(H)):
    spot = T - H[i] * 0.006
    if abs(spot - A) < mini:
        mini = abs(spot - A)
        res = i + 1
print(res)
