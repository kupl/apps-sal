(jewel, query) = map(int, input().split())
t = min(jewel, query)
dq = [int(i) for i in input().split()]
ans = []
for i in range(t + 1):
    for j in range(i + 1):
        have = dq[:j] + dq[jewel - i + j:]
        drop = query - len(have)
        for k in range(drop):
            if not have:
                break
            cand = min(have)
            if cand < 0:
                have.remove(cand)
            else:
                break
        ans.append(sum(have))
print(max(ans))
