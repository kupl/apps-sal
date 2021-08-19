(N, K) = map(int, input().split())
s = set(range(1, N + 1))
for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for x in A:
        try:
            s.remove(x)
        except:
            pass
print(len(s))
