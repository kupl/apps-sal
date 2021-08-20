(n, x) = map(int, input().split())
m = [int(input()) for i in range(n)]
print(len(m) + (x - sum(m)) // min(m))
