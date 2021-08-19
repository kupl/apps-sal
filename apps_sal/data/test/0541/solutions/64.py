(N, M) = list(map(int, input().split()))
AB = sorted([list(map(int, input().split())) for _ in range(M)])
AB = sorted(AB, reverse=False, key=lambda x: x[1])
last_b = AB[0][1] - 1
cnt = 1
for (a, b) in AB:
    if a <= last_b:
        continue
    else:
        last_b = b - 1
        cnt += 1
print(cnt)
