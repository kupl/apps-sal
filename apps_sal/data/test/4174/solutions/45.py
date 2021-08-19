(n, x) = list(map(int, input().split()))
l = list(map(int, input().split()))
ans = 0
bound = 0
for i in l:
    bound += i
    ans += 1
    if bound > x:
        break
else:
    ans = n + 1
print(ans)
