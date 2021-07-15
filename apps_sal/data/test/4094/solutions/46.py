k = int(input())
x = 7%k
ans = 1
for i in range(k):
    if x == 0:
        print(ans)
        break
    x = (10*x+7) % k
    ans += 1
else:
    print(-1)
