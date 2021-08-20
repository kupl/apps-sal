def gns():
    return list(map(int, input().split()))


(n, k) = gns()
ns = gns()
sm = [ns[-1]]
for i in reversed(list(range(n - 1))):
    sm.append(sm[-1] + ns[i])
ans = sm.pop()
sm.sort()
if k > 1:
    ans += sum(sm[-k + 1:])
print(ans)
