n = int(input())
x = list(map(int, input().split()))
for i in range(1, n + 1000):
    count = 0
    for j in range(n):
        count += (x[j] - i) * (x[j] - i)
    if i == 1:
        min = count
    elif count < min:
        min = count
    else:
        break
print(min)
