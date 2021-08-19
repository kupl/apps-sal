(K, X) = map(int, input().split())
start = X - K + 1
goal = X + K
lst = [i for i in range(start, goal)]
print(*lst)
