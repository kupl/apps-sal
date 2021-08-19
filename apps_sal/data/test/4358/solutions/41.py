N = int(input())
p = [int(input()) for i in range(N)]
a = sum(p)
print(int(a - max(p) / 2))
