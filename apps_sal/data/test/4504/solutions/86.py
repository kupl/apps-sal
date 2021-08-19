#n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
s = input()
n = len(s)


def isrepeat(s):
    res = False
    n = len(s)
    if s[0:n // 2] + s[0:n // 2] == s:
        res = True
    return res


for delnum in range(1, n):
    if (n - delnum) % 2 == 0:
        if isrepeat(s[0:n - delnum]):
            ans = n - delnum
            break
print(ans)
