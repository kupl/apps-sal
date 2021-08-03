n = int(input())
k = int(input())
l = list(map(int, input().split()))
c = 0
for x in l:
    c += min(x, k - x)
print(2 * c)
