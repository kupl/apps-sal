N = int(input())
p = 1
for i in range(N):
    p *= i + 1
    p %= 1000000007
print(p)
