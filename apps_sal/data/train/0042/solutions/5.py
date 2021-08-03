import sys
D = {}
m = 18
for i in range(1, 1 << m):
    D[bin(i)[2:]] = i
for _ in range(int(input())):
    S = sys.stdin.readline().rstrip()
    s = 0
    N = len(S)
    ans = 0
    for i in range(N):
        if S[i] == "1":
            for j in range(1, min(m, N - i) + 1):
                k = D[S[i:i + j]]
                if s + j >= k:
                    ans += 1
            s = 0
        else:
            s += 1
    print(ans)
