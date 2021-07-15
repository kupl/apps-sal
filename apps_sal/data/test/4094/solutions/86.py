k = int(input())
ans = -1
sm = 7
i = 1
if k % 2 == 0 or k % 5 == 0:
    ans = -1
elif sm % k == 0:
    ans = 1
else:
    for i in range(1, k):
        sm = (sm * 10 + 7) % k
        if sm == 0:
            ans = i + 1
            break
        i += 1
print(ans)

