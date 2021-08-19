(N, A, B) = map(int, input().split())
ls = []
for n in range(1, N + 1):
    sm = sum((int(s) for s in str(n)))
    if A <= sm <= B:
        ls.append(int(n))
print(sum(ls))
