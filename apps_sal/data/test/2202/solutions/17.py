n, p = map(int, input().split())
a = [int(x) for x in input().split()]
s = sum(a)
ans = -1; psum = 0
for i in a:
    psum += i
    ans = max(ans, psum % p + (s - psum) % p)
print(ans)
