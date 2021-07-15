n = int(input())
r = 0
for q in range(1, int(n ** (1 / 2))+1):
    if n % q == 0:
        r += 2
if n ** (1 / 2) // 1 == n ** (1 / 2):
    r -= 1
print(r)

