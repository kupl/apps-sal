
n = input()
a = list(map(int, input().split()))
ans = 0
k = 0
for i in a:
    ans += abs(i - k)
    k += (i - k)

print(ans)
