a = int(input())
b = list(map(int, input().split()))
total = 0
total2 = 0
i = 1
for i in range(a - 1):
    if b[i + 1] <= b[i]:
        total += 1
    else:
        if total2 <= total:
            total2 = total
        total = 0
print(max(total2, total))
