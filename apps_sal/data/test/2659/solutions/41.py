K = int(input())
 
def f(n):
    return n / sum([int(s) for s in str(n)])

ans = [1]
for k in range(K - 1):
    min_f_val, next_snuke = float('inf'), None
    n = str(ans[-1] + 1)
    for i in range(len(n)):
        for x in range(int(n[i]), 10):
            X = n[:i] + str(x) + '9' * (len(n) - i - 1)
            f_val = f(int(X))
            if f_val < min_f_val:
                next_snuke = int(X)
                min_f_val = f_val
    ans.append(next_snuke)
print(*ans, sep='\n')
