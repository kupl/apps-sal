import math
n, b, p = map(int, input().split())
curr = n
ans = 0
while curr != 1:
    l = 2 ** int(math.log(curr, 2))
    ans += l * b + l // 2
    curr -= (l // 2)
print(ans, n * p)
