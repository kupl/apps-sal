n = int(input())
print(sum(((x := (n // i)) * (x + 1) * i // 2 for i in range(1, n + 1))))
