(K, S) = map(int, input().split())
print(sum((0 <= S - x - y <= K for x in range(K + 1) for y in range(K + 1))))
