n = int(input())
mx = 1


def check(v):
    s = bin(v)[2:]
    k = s.count('1')
    if ('1' * k + '0' * (k - 1)) == s:
        return 1
    return 0


for i in range(1, n + 1):
    if n % i:
        continue
    if check(i) and i > mx:
        mx = i
print(mx)
