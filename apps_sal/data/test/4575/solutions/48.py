n = int(input())
d, x = map(int, input().split())
c = 0
for i in range(n):
    a = int(input())
    c += (d - 1) // a + 1
print(x + c)
