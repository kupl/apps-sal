n, k = map(int, input().split())
D = list(input().split())

ans = str(n)
while not all([c not in D for c in ans]) and int(ans) >= n:
    ans = str(int(ans) + 1)
print(ans)
