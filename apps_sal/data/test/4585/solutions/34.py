from math import floor
X = int(input())
for n in range(1, floor(X / 2) + 2):
    if n * (n + 1) // 2 >= X:
        ans = n
        break
print(ans)
