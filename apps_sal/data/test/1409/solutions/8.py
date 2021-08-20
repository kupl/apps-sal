(n, k) = map(int, input().split())
print(len([a for a in sorted(map(int, input().split())) if a <= 5 - k]) // 3)
