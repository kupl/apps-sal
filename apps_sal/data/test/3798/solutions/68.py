n = int(input())
s = int(input())

sqrt = 0
for i in range(n+1):
    if i*i >= n:
        sqrt = i
        break

def dsum(n, b):
    ret = 0
    while n :
        ret += n % b
        n //= b
    return ret


if s > n:
    print((-1))
    return
if s == n:
    print((n+1))
    return

# b = 2 ~ sqrt
# 少し先を見てもいい
for b in range(2, sqrt+1):
    use_n = n
    ans_tmp = dsum(n, b)
    if ans_tmp == s:
        print(b)
        return

# n = p*b + q
# s = p + q
# n = 2, s = 1 なら、 b=2, p=1, q=0
for p in range(1, sqrt)[::-1]:
    b = (n-s)//p + 1
    if b > 1 and dsum(n, b) == s:
        print(b)
        return
print((-1))

