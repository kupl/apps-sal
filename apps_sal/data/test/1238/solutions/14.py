n = int(input())

a = list(map(int, input().split()))

u, v = min(a), max(a)

print(v - u + 1 - n)
