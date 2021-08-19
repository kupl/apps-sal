N, K = map(int, input().split())
start = sum(range(K))
end = sum(range(N - K + 1, N + 1))
count = 0
#print(start, end)
for k in range(K, N + 2):
    count += end - start + 1
    count %= 1000000007
    start += k
    end += (N - k)

print(count)
