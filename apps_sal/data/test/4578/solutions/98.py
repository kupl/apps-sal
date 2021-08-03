n, x = map(int, input().split())
s = [int(input())for _ in range(n)]
p = (x - sum(s)) // min(s)
print(p + n)
