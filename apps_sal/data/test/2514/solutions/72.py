N = int(input())
A = list(map(int, input().split()))
a = {}
for i in A:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
Q = int(input())
ans = sum(A)
for i in range(Q):
    B, C = map(int, input().split())
    if B in a:
        ans += (C - B) * a[B]
        if C in a:
            a[C] += a[B]
        else:
            a[C] = a[B]
        a[B] = 0
    print(ans)
