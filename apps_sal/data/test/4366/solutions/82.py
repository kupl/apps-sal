
a, b = list(map(int, input().split()))

if (a + b) >= 24:
    answer = (a + b) - 24
else:
    answer = a + b
print(answer)
