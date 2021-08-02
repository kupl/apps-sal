n, k = map(int, input().split())
s = input()
ans1 = 0
ans = 0
a = list(input())
for i in range(n):
    if s[i] in a:
        ans += 1
    else:
        ans1 += (ans * (ans + 1) // 2)
        ans = 0
ans1 += (ans * (ans + 1)) // 2
print(ans1)
