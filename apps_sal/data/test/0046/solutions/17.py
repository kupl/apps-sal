n, m = list(map(int, input().split()))
cap = m // 5
others = m % 5

result = n * cap

cap2 = n // 5

result += cap2 * others

for i in range(cap2 * 5 + 1, cap2 * 5 + (n % 5) + 1):
    for j in range(cap * 5 + 1, cap * 5 + others + 1):
        if (i + j) % 5 == 0:
            result += 1

print(result)
