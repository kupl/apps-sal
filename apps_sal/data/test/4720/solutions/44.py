# https://atcoder.jp/contests/abc073/tasks/abc073_b
N = int(input())
ans = 0
for i in range(N):
    st, sp = map(int, input().split())
    ans += abs(sp - st + 1)
print(ans)
