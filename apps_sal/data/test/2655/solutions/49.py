n = int(input())
a_list = sorted([int(x) for x in input().split()])
ans = a_list.pop()
n -= 2
while n > 0:
    a = a_list.pop()
    ans += a
    n -= 1
    if n > 0:
        ans += a
        n -= 1
print(ans)
