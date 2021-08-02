N = int(input())

a = 1
div = 10**9 + 7

for n in range(1, N + 1):
    a *= n
    if a > div:
        a = a % div

print(a)
