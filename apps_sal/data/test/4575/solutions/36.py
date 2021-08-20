n = int(input())
(d, x) = map(int, input().split())
res = x
for i in range(n):
    a = int(input())
    res += (d - 1) // a + 1
print(res)
