a, b, c = map(int, input().split())
k = int(input())
m = max(a, b, c)

for i in range(k):
    m *= 2

print(sum([a, b, c]) - max(a, b, c) + m)
