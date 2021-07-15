def factor(n):
    ans = set()
    q = 2
    while q * q <= n:
        if n % q == 0:
            ans.add(q)
            n //= q
        else:
            q += 1
    if n > 1:
        ans.add(n)
    return ans
n = int(input())
num = 1
q_n_set = factor(n)
for i in q_n_set:
    num *= i
print(num)

