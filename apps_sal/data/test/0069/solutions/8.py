T = int(input())
for _ in range(T):
    n, x = map(int, input().split())
    S = input()
    A = [0] * n
    for i, s in enumerate(S):
        A[i] = A[i-1] + (1 if s == "0" else -1)
    t = A[-1]
    A[-1] = 0
    if t > 0:
        print(len([a for a in A if (x-a) % t == 0 and a <= x]))
    elif t < 0:
        print(len([a for a in A if (x-a) % (-t) == 0 and a >= x]))
    else:
        print(-1 if A.count(x) else 0)
