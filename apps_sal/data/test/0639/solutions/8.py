n, x = list(map(int, input().split()))

a = set(map(int, input().split()))
result = 0
for i in range(x):
    if i not in a:
        result += 1

if x in a:
    result += 1

print(result)

