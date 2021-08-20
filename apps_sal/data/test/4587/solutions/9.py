import bisect
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a = sorted(a)
b = sorted(b)
c = sorted(c)
ans = 0
for i in range(n):
    B = b[i]
    b_in = bisect.bisect_left(a, B)
    if b_in == 0:
        continue
    c_in = bisect.bisect_right(c, B)
    c_cnt = n - c_in
    ans += b_in * c_cnt
print(ans)
