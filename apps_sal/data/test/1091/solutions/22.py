n = int(input())
p = list(map(int, input().split()))

a = p.index(max(p)) + 1
p.remove(max(p))
b = max(p)

print(a, b)
