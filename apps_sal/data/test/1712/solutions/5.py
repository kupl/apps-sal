(n, x, y) = map(int, input().split())
result = []
for _ in range(n):
    a = int(input())
    vanya_hits = x * (a + 1) // (x + y)
    vova_hits = y * (a + 1) // (x + y)
    if vanya_hits / x == vova_hits / y:
        result.append('Both')
    elif vanya_hits / x > vova_hits / y:
        result.append('Vanya')
    else:
        result.append('Vova')
print(*result, sep='\n')
