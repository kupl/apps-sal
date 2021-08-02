n, m = map(int, input().split())
SC = [list(map(int, input().split())) for _ in range(m)]

for i in range(10**n):
    if len(str(i)) == n and all(str(i)[s - 1] == str(c) for s, c in SC):
        print(i)
        break
else:
    print(-1)
