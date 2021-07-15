n, q = list(map(int, input().split()))

qs = []
ans = [0] * q
used = [0] * n

for _ in range(q):
    t, k, d = list(map(int, input().split()))
    less = min(sum(used[i] <= t for i in range(n)), k)
    
    if less >= k:
        for i in range(n):
            if less == 0: break
            if used[i] <= t:
                used[i] = t + d
                ans[_] += i + 1
                less -= 1
    else:
        ans[_] = -1

print("\n".join(map(str, ans)))


