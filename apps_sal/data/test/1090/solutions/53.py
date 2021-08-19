import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
(n, k) = list(map(int, input().split()))
s = input()
cnt = 0
for i in range(n):
    if s[i] == s[i + 1]:
        cnt += 1
ans = min([k * 2 + cnt, n - 1])
print(ans)
