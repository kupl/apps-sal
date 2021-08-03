n = int(input())
d, x = map(int, input().split())
lst = [int(input()) for _ in range(n)]

res = x
for i in lst:
    res += ((d - 1) // i) + 1
print(res)
