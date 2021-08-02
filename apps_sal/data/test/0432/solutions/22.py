import sys
readline = sys.stdin.readline


N = int(readline())
C = list(map(int, readline().split()))
A = list(map(lambda x: int(x) - 1, readline().split()))


inf = 10**9
used = set()
ans = 0
for i in range(N):
    if i in used:
        continue
    seen = set()
    stack = [i]
    cnt = 0
    st = None
    while stack:
        vn = stack.pop()
        vf = A[vn]
        if vf in used:
            break
        if vf in seen:
            st = vf
            break
        seen.add(vf)
        stack.append(vf)

    if st is not None:
        vn = st
        cnt = C[vn]
        vf = A[vn]
        vn = A[vn]
        while vn != st:
            cnt = min(cnt, C[vn])
            vn = A[vn]
    used |= seen
    ans += cnt
print(ans)
