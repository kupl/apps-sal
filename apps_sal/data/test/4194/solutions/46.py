(N, M) = map(int, input().split())
day = list(map(int, input().split()))
if sum(day) > N:
    print(-1)
else:
    print(N - sum(day))
