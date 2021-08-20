(N, *A) = map(int, open(0).read().split())
cnt = 0
for a in A:
    for n in range(1, 31):
        if a % 2 ** n != 0:
            cnt += n - 1
            break
print(cnt)
