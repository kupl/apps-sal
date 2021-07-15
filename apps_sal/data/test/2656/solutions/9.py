n = int(input())
s = input()
 
S = len(s)
mod = 10 ** 9 + 7
 
tmp_ans = pow(26, n, mod)
div = pow(26, -1, mod)
 
ans = tmp_ans
 
for i in range(1, n+1):
    tmp_ans = (tmp_ans * 25 * div) % mod
    tmp_ans = ((tmp_ans * (S-1+i)) * pow(i, -1, mod)) % mod
    ans = (ans + tmp_ans) % mod
 
ans %= mod
 
print(ans)
