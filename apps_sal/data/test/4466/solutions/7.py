x, y, z = map(int, input().split())

result = 0
while y * result + z * (result + 1) <= x:
    result += 1

print(result - 1)
