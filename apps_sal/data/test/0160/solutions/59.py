def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
n, k = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
l = make_divisors(s)
l.sort(reverse=True)
for i in l:
    l2 = [j % i for j in a]
    l2.sort(reverse=True)
    m = sum(l2) - sum(l2[:sum(l2)//i])
    if i == 1:
        m = 0
    if m <= k:
        s = i
        break
print(s)
