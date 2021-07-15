import string

def zero_count(n):
    return bin(63 - n).count('1')

E = string.digits + string.ascii_uppercase + string.ascii_lowercase + '-_'
D = {c : zero_count(i) for (i,c) in enumerate(E)}

p = 10 ** 9 + 7
s = input().rstrip()
ans = sum(D[c] for c in s)
print(pow(3, ans, p))

