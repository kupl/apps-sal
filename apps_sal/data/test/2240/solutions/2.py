s = input()
t = input()

n,m = len(s), len(t)
a = s.count('0')
b = len(s) - a


pow = [1] * m
h = [0] * (m+1)
p, mod = 31, 10**9+9
for i in range(1, m):
    pow[i] = pow[i-1] * p % mod

for i in range(m):
    h[i+1] = (h[i] + (ord(t[i])-ord('a')+1) * pow[i]) % mod


def get_hash(i, j):
    hash_value = (h[j] - h[i] + mod) % mod
    hash_value = (hash_value * pow[m-i-1]) % mod
    return hash_value


def check(x, y):
    index = 0
    hash_x = hash_y = -1
    for i in range(n):
        if s[i] == '0':
            if hash_x == -1:
                hash_x = get_hash(index, index+x)
            else:
                if get_hash(index, index+x) != hash_x: return False
            index += x
        else:
            if hash_y == -1:
                hash_y = get_hash(index, index+y)
            else:
                if get_hash(index, index+y) != hash_y: return False
            index += y
    return hash_x != hash_y


res = 0
for x in range(1, m//a+1):
    if (m - a*x) % b == 0:
        y = (m - a*x) // b
        if y == 0: continue
        if check(x ,y):
            res += 1

print(res)
