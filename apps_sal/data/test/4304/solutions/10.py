a, b = map(int, input().split())
d = b - a 

print(sum(i for i in range(1, d)) - a)
