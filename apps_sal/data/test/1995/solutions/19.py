s = input()
m = int(input())
for i in range(m):
    l, r, k = map(lambda x: int(x) - 1, input().split())
    k += 1
    d = r - l + 1
    k %= d
    s = s[0:l] + s[r-k+1:r+1] + s[l:r-k+1] + s[r+1:]
print(s)
