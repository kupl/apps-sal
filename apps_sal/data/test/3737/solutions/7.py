n = int(input())
a = list(map(int, input().split()))

r = 0

min_a = min(a)
max_a = max(a)

for i in a:
    if i > min_a and i < max_a:
        r += 1
print(r)
