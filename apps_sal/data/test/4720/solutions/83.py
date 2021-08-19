N = int(input())
print(sum((r - l + 1 for (l, r) in (map(int, input().split()) for _ in range(N)))))
