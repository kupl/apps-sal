n, m = list(map(int, input().split()))
Max = max(0, (n - m + 1) * (n - m) // 2)
Mi = n % m
Ma = m - Mi
Min = Ma * (n // m) * (n // m - 1) // 2 + Mi * (n // m) * (n // m + 1) // 2
print(Min, Max)
