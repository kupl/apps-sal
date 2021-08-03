def divisor(n):
    lower, upper = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower.append(i)
            if i != n // i:
                upper.append(n // i)
        i += 1
    return lower + upper[::-1]


n = int(input())
ans = float("inf")
for d in divisor(n):
    i = n // d
    tmp = i + d - 2
    ans = min(ans, tmp)
print(ans)
