n = int(input())
k = int(input())
a = int(input())
b = int(input())
#inf = 100000000000000000000000000000;
ost = 0
res = 0
while a * (n // k) + b + (n % k) * a < n * a:
    ost = ost + (n % k) * a
    res = res + b
    n = n // k
# print(n);
# print(res);
# print(ost);
res = res + (n - 1) * a + ost
print(res)
