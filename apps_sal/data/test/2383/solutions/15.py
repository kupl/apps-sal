n = int(input())
a = list(map(int, input().split()))

c = 1
for i in a:
    if i == c:
        c += 1
print(n - c + 1 if c > 1 else -1)
