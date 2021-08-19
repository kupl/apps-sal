l = input()[::-1]
ans = 1
mod = 10 ** 9 + 7
for i in range(len(l)):
    if l[i] == '1':
        ans = (ans * 2 + pow(3, i, mod)) % mod
print(ans)
