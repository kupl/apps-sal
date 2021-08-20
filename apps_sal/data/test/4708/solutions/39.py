n = int(input())
k = int(input())
x = int(input())
y = int(input())
if n > k:
    answer = k * x + (n - k) * y
else:
    answer = n * x
print(answer)
