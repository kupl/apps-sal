a = int(input())
b = list(map(int, input().split()))
b.sort()
c = b[0]
for i in range(1, a):
    c += b[i]
    c /= 2
print(c)
