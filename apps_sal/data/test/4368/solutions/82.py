N, K = map(int, input().split())
i = 0
while N >= K ** i:
    i += 1
else:
    print(i)
