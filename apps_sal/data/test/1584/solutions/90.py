n = int(input())
l_ls = list(map(int, input().split()))
l_ls.sort()
def check(a,b,c):
    return abs(a-b) < c < a+b
ans = 0
for i in range(n):
    short = l_ls[i]
    num = 0
    r = i+1
    for l in range(i+1,n):
        while r+1 < n and check(short, l_ls[l], l_ls[r+1]):
            r += 1
        num += r - l
        if r == l:
            r += 1
    ans += num
print(ans)
            

