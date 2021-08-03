n, x = map(int, input().split())
m = [int(input()) for m in range(n)]
print(len(m) + (x - sum(m)) // min(m))
