from sys import stdin, stdout
import math

t = int(stdin.readline())
for _ in range(t):
    n, k = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    w = list(map(int, stdin.readline().split()))

    a = sorted(a)
    w = sorted(w)
    st, end = 0, n - 1
    ans = 0
    idx = 0
    while idx < k and w[idx] == 1:
        ans += a[end] * 2
        end -= 1
        idx += 1
    for i in range(k - 1, idx - 1, -1):
        wi = w[i]
        ans += a[st] + a[end]
        end -= 1
        st += wi - 1
    print(ans)
