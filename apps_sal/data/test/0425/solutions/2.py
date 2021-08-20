(n, p) = list(map(int, input().split()))
ans = 1
n2 = n
while n2 > 0:
    n2 = n - ans * p
    count1 = bin(n2).count('1', 2)
    if count1 <= ans and ans <= n2:
        print(ans)
        break
    ans += 1
else:
    print(-1)
