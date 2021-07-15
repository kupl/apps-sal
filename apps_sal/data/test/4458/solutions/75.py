N = int(input())
P = list(map(int, input().split()))
Min = P[0]
count = 0
for i in range(N):
    if Min >= P[i]:
        count += 1
        Min = P[i]
print(count)
