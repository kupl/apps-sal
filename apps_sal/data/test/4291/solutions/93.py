N, Q = list(map(int, input().split()))
S = input()

c = [0 for _ in range(N + 1)]
for i in range(1, N):
    a = 0
    if S[i - 1:i + 1] == 'AC':
        a = 1
    c[i + 1] = c[i] + a

for _ in range(Q):
    l, r = list(map(int, input().split()))
    l -= 1
    result = c[r] - c[l]
    if l > 0 and S[l - 1:l + 1] == 'AC':
        result -= 1
    print(result)
