def gcd(a, b):
    """a, bの最大公約数(greatest common divisor:GCD)を求める"""
    if b == 0:
        return a
    return gcd(b, a%b)


def lcm(a, b):
    """a, bの最小公倍数(least common multiple:LCM)を求める"""
    return (a * b) // gcd(a, b)


def multi_gcd(array: list) -> int:
    """arrayのGCDを求める"""
    ans = array[0]
    for i in range(1, len(array)):
        ans = gcd(ans, array[i])
    return ans


def multi_lcm(array):
    """arrayのLCMを求める"""
    ans = array[0]
    for i in range(1, len(array)):
        ans = (ans * array[i]) // gcd(ans, array[i])
    return ans


n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
li_a = []
for i in range(n-1):
    tmp = a[i+1] - a[i]
    if tmp != 0:
        li_a.append(tmp)
gcd_a = multi_gcd(li_a)
max_a = max(a)
ans = 0
for i in range(n):
    ans += (max_a - a[i]) // gcd_a
print(ans, gcd_a)



