s = input()
m = int(input())
a = list(map(int, input().split()))
n = len(s)

flip = [0 for i in range(n)]
for x in a:
    x -= 1
    flip[x] ^= 1
    if x > 0:
        flip[n - x] ^= 1

for i in range(1, n):
    flip[i] ^= flip[i - 1]

ans = ['a' for i in range(n)]
for i in range(n):
    if flip[i] == 1:
        ans[i] = s[n - i - 1]
    else:
        ans[i] = s[i]

print(''.join(ans))

