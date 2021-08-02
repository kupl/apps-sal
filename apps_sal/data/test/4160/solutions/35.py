x = int(input())
curr = 100
ans = 0
while curr < x:
    curr = curr + curr // 100
    ans += 1
print(ans)
