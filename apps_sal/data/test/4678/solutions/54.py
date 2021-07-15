n = int(input())
aaa = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    diff = aaa[i] - aaa[i - 1]
    if diff < 0:
        aaa[i] -= diff
        ans -= diff
print(ans)
