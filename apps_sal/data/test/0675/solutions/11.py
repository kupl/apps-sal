a, b, c = map(int, input().split())
t = sorted(map(int, input().split()), reverse=True)
if c > b:
    print('-1')
else:
    q = [False] * 600
    for k in t:
        k = k - b
        for j in range(k, k + c - sum(q[i] for i in range(k, k + b))):
            q[j] = True
    print(sum(q))
