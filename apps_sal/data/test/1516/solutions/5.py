n = int(input())
l = list(map(int, input().split()))
answer = 0
mod = 998244353
for val in l:
    itr = 0
    while val > 0:
        cur = val % 10
        val //= 10
        answer += n * cur * (10 ** itr) % mod
        itr += 1
        answer += n * cur * (10 ** itr) % mod
        itr += 1
        answer %= mod
print(answer)
