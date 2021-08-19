n = int(input())
la = list(map(int, input().split()))
lb = list(map(int, input().split()))
count = 0
for i in range(n):
    count += min(la[i], lb[i])
    if la[i] < lb[i]:
        if la[i + 1] >= lb[i] - la[i]:
            count += lb[i] - la[i]
            la[i + 1] -= lb[i] - la[i]
        else:
            count += la[i + 1]
            la[i + 1] = 0
print(count)
