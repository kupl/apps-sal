N = int(input())
H = list(map(int, input().split()))
result = 0
count = 0
for i in range(len(H) - 1):
    if H[i + 1] <= H[i]:
        count += 1
        if result < count:
            result = count
    else:
        count = 0
print(result)
