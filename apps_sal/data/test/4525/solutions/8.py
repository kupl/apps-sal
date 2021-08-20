t = int(input())
for _ in range(t):
    n = int(input())
    if n // 2 % 2 == 1:
        print('NO')
    else:
        print('YES')
        even = [i * 2 for i in range(1, n // 2 + 1)]
        odd = [i * 2 - 1 for i in range(1, n // 2)]
        odd.append(sum(even) - sum(odd))
        print(*even, *odd)
