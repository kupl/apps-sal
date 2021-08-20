(N, T) = map(int, input().split())
List = list(map(int, input().split()))
res = 0
for i in range(1, N):
    sumsum = List[i] - List[i - 1]
    if sumsum >= T:
        res += T
    else:
        res += sumsum
res += T
print(res)
