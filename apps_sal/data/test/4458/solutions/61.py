N = int(input())
P = list(map(int, input().split()))
cnt = 0
mini = float('inf')
for i in range(0, len(P)):
    if P[i] < mini:
        cnt += 1
        mini = P[i]
print(cnt)
