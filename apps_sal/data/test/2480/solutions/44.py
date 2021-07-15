import collections
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
table = collections.defaultdict(int)

ans = 0
s = [0]*(N+1)
a = set()
for i in range(N):
    s[i+1] = s[i]+A[i]

s = [(s[i]-i) % K for i in range(N+1)]
for i in range(N+1):
    ans += table[s[i]]  # i番目まで取る組み合わせの数
    table[s[i]] += 1
    if i >= K-1:
        # Kで割ったあまりがKを超えることはないので、期限切れのものを引く
        table[s[i-K+1]] -= 1

print(ans)

