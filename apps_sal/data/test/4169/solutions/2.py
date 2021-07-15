N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort(key=lambda x : x[0])
ans = 0
for AB in AB:
    if M <= AB[1]:
        ans += M * AB[0]
        break
    else:
        ans += AB[0] * AB[1]
        M -= AB[1]
print(ans)
