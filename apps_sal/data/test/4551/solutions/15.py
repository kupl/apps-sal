

a, b, c, d = list(map(int, input().split()))

result = "ret"

if (a + b) > (c + d):
    result = "Left"
elif (a + b) < (c + d):
    result = "Right"
else:
    result = "Balanced"

print(result)
