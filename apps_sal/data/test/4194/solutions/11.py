(n, m) = map(int, input().split())
a = list(map(int, input().split()))
a_t = sum(a)
if n < a_t:
    print('-1')
else:
    print(n - a_t)
