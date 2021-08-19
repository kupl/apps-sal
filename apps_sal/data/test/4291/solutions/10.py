N, Q = map(int, input().split())
S = input()

# 累積和的な発想
t = [0] * N
for i in range(N - 1):
    t[i + 1] = t[i]
    if S[i:i + 2] == 'AC':
        t[i + 1] += 1

for _ in range(Q):
    l, r = map(int, input().split())
    print(t[r - 1] - t[l - 1])
