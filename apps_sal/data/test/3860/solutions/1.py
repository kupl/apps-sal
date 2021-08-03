b = int(input())
g = int(input())
n = int(input())

res = 0
for i in range(n + 1):
    if i <= b and (n - i) <= g:
        res += 1

print(res)
