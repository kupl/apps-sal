n = int(input())
num = 0
for a in range(1, n + 1):
    for b in range(a, n + 1):
        if b <= a ^ b <= n:
            if a + b > a ^ b:
                num += 1
print(num)
