N = int(input())

def prime_check(n):
    for i in range(2,int(n/2)+1):
        if n % i == 0:
            return False
    return True

def factor(n):
    tmp = n
    out = [0] * len(prime_nums)
    i = 0
    while tmp != 1:
        if tmp % prime_nums[i] == 0:
            tmp = tmp // prime_nums[i]
            out[i] += 1
        else:
            i += 1
    return out
        
prime_nums = [k for k in range(2, N+1) if prime_check(k)]
memo = []
for i in range(1, N+1):
    memo.append(factor(i))

record = [0] * len(prime_nums)
for p in range(len(prime_nums)):
    for j in range(N):
        record[p] = max(record[p], memo[j][p])
        
ans = 1
for i in [b**a for a, b in zip(record, prime_nums)]:
    ans *= i

print(ans+1)
