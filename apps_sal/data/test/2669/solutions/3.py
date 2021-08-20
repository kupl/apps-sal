ans = []


def printMaxActivities(s, f):
    n = len(f)
    i = 0
    ans.append(i)
    for j in range(n):
        if s[j] >= f[i]:
            ans.append(j)
            i = j


n = int(input())
s = list(map(int, input().split()))
f = list(map(int, input().split()))
printMaxActivities(s, f)
print(*ans)
