K,X = map(int,input().split())
first = X - K + 1
second = X + K - 1
if first < -1000000:
    first = -1000000
if second > 1000000:
    second = 1000000
ans = list(range(first,second + 1))
print(*ans)
