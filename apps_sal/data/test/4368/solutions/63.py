(N, K) = map(int, input().split())
ans_str = ''
n = N
while n >= K:
    n = n // K
    ans_str += str(n % K)
ans_str += str(n)
print(len(ans_str))
