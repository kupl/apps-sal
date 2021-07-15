def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))

n = getN()
mid = n * 2 -1
ans = -mid
while(mid > 0):
    ans += mid*2
    mid -= 2

print(ans)
