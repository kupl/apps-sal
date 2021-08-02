t = int(input())
for q in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = min(a) * max(a)
    deliver = [q for q in range(2, round(ans**(1 / 2)) + 1) if ans % q == 0]
    if deliver + [ans // deliver[q] for q in range(len(deliver) - 1 - (deliver[-1]**2 == ans), -1, -1)] == sorted(a):
        print(ans)
    else:
        print(-1)
