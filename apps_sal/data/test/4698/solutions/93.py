N = int(input())
T = list(map(int, input().split()))
M = int(input())
ans = sum(T)
copy = ans
for i in range(M):
    p, x = list(map(int, input().split()))
    p -= 1
    ans -= T[p]
    ans += x
    print(ans)
    ans = copy
