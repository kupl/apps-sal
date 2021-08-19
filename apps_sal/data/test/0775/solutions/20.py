(n, m, k) = map(int, input().split())
h = set(map(int, input().split()))
answer = 1
if answer in h:
    print(answer)
else:
    for i in range(k):
        (u, v) = map(int, input().split())
        if u == answer:
            answer = v
        elif v == answer:
            answer = u
        else:
            continue
        if answer in h:
            break
    print(answer)
