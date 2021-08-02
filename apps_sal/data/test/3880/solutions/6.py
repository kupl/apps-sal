3

n = int(input())
data = list(map(int, input().split()))

x = 0
for element in data:
    if element < 0:
        x += 1

values = sorted(list(map(abs, data)))
result = sum(values)
if n % 2 == 0 and x % 2 == 1:
    result -= 2 * values[0]

print(result)
