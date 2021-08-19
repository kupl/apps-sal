N = int(input())
s = [int(input()) for _ in range(N)]
s.sort()
mod = [i % 10 for i in s]
ans = sum(s)
if ans % 10 == 0:
    if mod.count(0) == N:
        ans = 0
    else:
        for i in range(N):
            if mod[i] != 0:
                ans -= s[i]
                break
print(ans)
