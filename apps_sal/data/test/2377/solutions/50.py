import sys
input = sys.stdin.readline
n, h = map(int, input().split())
a, b = [0]*n, [0]*n
for i in range(n):
    a[i], b[i] = map(int, input().split())
a_max = max(a)
b_thr = []
for i in b:
    if i > a_max:
        b_thr.append(i)
b_thr.sort(reverse=True)
ans = 0
for i in b_thr:
    if h > 0:
        h -= i
        ans += 1
    else:
        print(ans)
        return
if h % a_max == 0:
    ans += h // a_max
else:
    ans += h // a_max + 1
print(ans)
