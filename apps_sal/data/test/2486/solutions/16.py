N, K = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse = True)

ans = 0
tmp = 0
for i in a:
    if tmp + i < K:
        ans += 1
        tmp += i
    else:
        ans = 0 #リセット

print (ans)
