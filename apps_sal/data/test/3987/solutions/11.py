n = int(input())
a = list(map(int, input().split()))
count = [0] * 4
for i in range(n):
    if a[i] == 1:
        count[0] += 1
        count[2] = max(count[1] + 1, count[2] + 1)
    else:
        count[1] = max(count[1] + 1, count[0] + 1)
        count[3] = max(count[3] + 1, count[2] + 1)
print(max(count))
