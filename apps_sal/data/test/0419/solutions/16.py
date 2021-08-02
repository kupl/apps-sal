x = int(input(), 2)
ans = 0
curr = 1
while curr < x:
    curr *= 4
    ans += 1
print(ans)
