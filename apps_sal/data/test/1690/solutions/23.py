n = int(input())
s = [int(i) for i in input().split()]
s = s[::-1]
c = 100000000000
ans = 0
for i in s:
    if i < c:
        c = i
    else:
        c = max(c - 1, 0)
    ans += c
print(ans)
