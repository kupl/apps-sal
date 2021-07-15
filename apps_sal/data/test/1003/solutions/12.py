n, m = map(int, input().split())

aux = [1 for i in range(n + 1)]
ans = 0
i = 1
while i < len(aux):
    
    if i % m == 0:
        aux.append(1)
    ans += 1
    i += 1

print(ans)
