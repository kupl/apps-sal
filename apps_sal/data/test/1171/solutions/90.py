N, K = list(map(int, input().split()))
V = list(map(int, input().split()))

ans = []
# きっちりK回しなくていいみたい
for left in range(N + 1):
    for right in range(N + 1):
        if left + right > N:
            break

        li = V[:left] + V[N - right:]
        li = sorted(li)

        d = K - left - right
        if d < 0:
            break

        c = sum(li)
        for i in range(min(d, len(li))):
            if li[i] < 0:
                c -= li[i]
            else:
                break

        ans.append(c)

print((max(ans)))
