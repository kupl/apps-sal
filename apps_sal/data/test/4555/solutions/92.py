a, b, k = map(int, input().split())
r = range(a, b+1)
print(*sorted(set(r[:k]) | set(r[-k:])), sep='\n')
