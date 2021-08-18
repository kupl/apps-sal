

a, b, c = list(map(int, input().split()))

result = "ret"
if (a + b) == c:
    result = "Yes"
elif (a + c) == b:
    result = "Yes"
elif (b + c) == a:
    result = "Yes"
else:
    result = "No"

print(result)
