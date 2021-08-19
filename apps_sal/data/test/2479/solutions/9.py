import sys
input = sys.stdin.readline
(n, q) = map(int, input().split())
left = n
up = n
ans = (n - 2) * (n - 2)
fixed_yoko = [0] * (n + 1)
fixed_tate = [0] * (n + 1)
post_process = []
for _ in range(q):
    (t, x) = map(int, input().split())
    if t == 1:
        if x > left:
            post_process.append((t, x))
        else:
            fixed_yoko[left] += -up
            fixed_yoko[x + 1] += up
            ans -= up - 2
            left = x
    elif t == 2:
        if x > up:
            post_process.append((t, x))
        else:
            fixed_tate[up] += -left
            fixed_tate[x + 1] += left
            ans -= left - 2
            up = x
for i in range(1, n + 1):
    fixed_yoko[i] += fixed_yoko[i - 1]
    fixed_tate[i] += fixed_tate[i - 1]
for (t, x) in post_process:
    if t == 1:
        ans -= fixed_yoko[x] - 2
    elif t == 2:
        ans -= fixed_tate[x] - 2
print(ans)
