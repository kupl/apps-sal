N, A, B = list(map(int, input().split()))

total = 0
for i in range(1, N + 1):
    subTotal = sum(list(map(int, str(i))))
    if subTotal >= A and subTotal <= B:
        total += i

print(total)
