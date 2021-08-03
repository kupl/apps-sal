def get_input_list():
    return list(map(int, input().split()))


n, m = get_input_list()
a = input()
b = input()
l = 0
q = 1
v = 0
i = n - 1
j = m - 1
r = 0
mod = 998244353
while j >= 0:
    if i >= 0 and a[i] == '1':
        v = (v + q) % mod
    if b[j] == '1':
        r = (r + v) % mod
    i -= 1
    q = (q << 1) % mod
    j -= 1
print(r)
