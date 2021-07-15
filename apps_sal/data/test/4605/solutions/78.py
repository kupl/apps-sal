N, A, B = map(int, input().split())

res = []

for n in range(1, N+1):
    i = list(str(n))
    i = [int(n) for n in i]
    if A <= sum(i) <= B:
        res.append(int(n))

print(sum(res))
