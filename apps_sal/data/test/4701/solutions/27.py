n = int(input())
k = int(input())
given_integer = 1
for i in range(0, n):
    given_integer = min(given_integer * 2, given_integer + k)
print(int(given_integer))
