n = int(input())

ret = 1

for i in range(n):
    ret *= i + 1
    ret %= 10**9 + 7
print(ret)
