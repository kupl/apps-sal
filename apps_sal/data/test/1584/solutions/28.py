n = int(input())
a_ls = list(map(int, input().split()))
def isOK(a,b,c):
    return abs(a-b) < c < a+b
a_ls.sort()
ans = 0
for i in range(n):
    short = a_ls[i]
    r = i+1
    num = 0
    for l in range(i+1,n-1):
        while r+1 < n and isOK(short, a_ls[l], a_ls[r+1]):
            r += 1
        num += r - l
        if l == r:
            r += 1
    ans += num
print(ans)
