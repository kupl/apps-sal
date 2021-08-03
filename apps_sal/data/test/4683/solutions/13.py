n = int(input())
a = list(map(int, input().split()))
suma = sum(a)
c = 0
for num in a:
    c += num**2
print((suma**2 - c) // 2 % (10**9 + 7))
