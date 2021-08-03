n = int(input())
data = [int(input()) for i in range(5)]
m = min(data)
if n % m == 0:
    print(4 + n // m)
else:
    print(5 + n // m)
