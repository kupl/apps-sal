n, m = map(int, input().split())
sc = [tuple(map(int, input().split())) for j in range(m)]
for i in range(10**n):
    if len(str(i)) == n and all(str(i)[s - 1] == str(c) for s, c in sc):
        print(i)
        break
else:
    print(-1)
