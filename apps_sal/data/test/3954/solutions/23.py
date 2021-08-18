n, kr = map(int, input().split())
l = list(map(int, input().split()))
ans = -2e18
for i in range(n):
    for j in range(i, n):
        k = kr
        sub = l[i:j + 1]
        sub_sum = sum(sub)
        sub.sort()
        chk = l[0:i] + l[j + 1:]
        chk.sort()
        chk.reverse()
        ans = max(ans, sub_sum)
        for t in range(len(sub)):
            if t < len(chk) and k > 0:
                if sub[t] < chk[t]:
                    sub_sum -= sub[t]
                    sub_sum += chk[t]
                    ans = max(ans, sub_sum)
                    k -= 1
            else:
                break
print(ans)
