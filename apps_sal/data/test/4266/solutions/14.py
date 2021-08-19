(k, x) = map(int, input().split())
start = max(-1000000, x - k + 1)
end = min(1000000, x + k - 1)
for i in range(start, end + 1):
    print(i, end=' ')
