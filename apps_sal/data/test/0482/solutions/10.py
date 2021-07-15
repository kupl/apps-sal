n, k = list(map(int, input().split()))
s = 'abcdefghijklmnopqrstuvwxyz'
res = ""
for i in range(n):
    res += s[i%k]

print(res)

