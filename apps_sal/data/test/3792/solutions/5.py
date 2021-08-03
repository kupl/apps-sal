# x = int(input())
# m, n = map(int, input().split())
# nums = list(map(int, input().split()))
n, k = list(map(int, input().split()))
s1 = input()
s2 = input()
cnt = 1
ans = 0
for i in range(n):
    cnt *= 2
    if s1[i] == 'b':
        cnt -= 1
    if s2[i] == 'a':
        cnt -= 1
    cnt = min(1e18 + 7, cnt)
    ans += min(cnt, k)
print(ans)
