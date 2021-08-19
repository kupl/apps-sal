(n, m, r) = map(int, input().split())
A = min(list(map(int, input().split())))
B = max(list(map(int, input().split())))
if B <= A:
    print(r)
else:
    ans = r % A + r // A * B
    print(ans)
