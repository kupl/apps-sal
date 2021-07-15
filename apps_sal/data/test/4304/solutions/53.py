a,b = map(int,input().split())
n = b - a
real_b = n * (n + 1) // 2

print(real_b - b)
