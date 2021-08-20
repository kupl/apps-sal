(n, m) = map(int, input().split())
sc = [tuple(map(int, input().split())) for j in range(m)]
for i in range(0 if n == 1 else 10 ** (n - 1), 10 ** n):
    if all((str(i)[s - 1] == str(c) for (s, c) in sc)):
        print(i)
        break
else:
    print(-1)
