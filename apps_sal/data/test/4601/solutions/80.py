(N, K) = map(int, input().split())
H = list(map(int, input().split()))
if N <= K:
    print(0)
elif K == 0:
    print(sum(H))
else:
    total = 0
    for i in H:
        total += i
    max_hp = sum(sorted(H, reverse=True)[:K])
    print(total - max_hp)
