a, b, c, d = map(int, input().split())

print(min (b, d) - max(a, c)) if min (b, d) > max(a, c) else print(0) 
