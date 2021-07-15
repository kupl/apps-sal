N,K = list(map(int,input().split()))

ans = 0
while True:
    if not N - K**ans >= 0:
        print(ans)
        break
    else:
        ans += 1

