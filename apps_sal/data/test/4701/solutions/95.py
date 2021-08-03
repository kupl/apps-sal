n = int(input())
k = int(input())
c = 1
for i in range(n):
    c = min(2 * c, c + k)
print(c)
