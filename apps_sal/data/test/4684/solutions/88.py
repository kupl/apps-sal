

r, g, b = list(map(int, input().split()))

input_rgb = r * 100 + g * 10 + b
result = "ret"

if input_rgb % 4 == 0:
    result = "YES"
else:
    result = "NO"

print(result)
