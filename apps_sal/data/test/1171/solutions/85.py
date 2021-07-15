n, k = list(map(int, input().split()))
v = list(map(int, input().split()))

res = 0
r = min(n, k)
for i in range(r+1):
    for j in range(r-i+1):
        in_hand = v[:i] + v[n-j:] if i + j < n else v[:]
        in_hand.sort(reverse=True)
        for _ in range(k-len(in_hand)):
            if not in_hand or in_hand[-1] >= 0:
                break
            in_hand.pop()
        res = max(res, sum(in_hand))
print(res)

