import collections

def f(myList):
    ans = ''
    if len(myList)%2==0:
        for i in range(len(myList)):
            ans += str(myList[i]) + ' '
    else:
        for i in range(len(myList)):
            ans += str(myList[-(i+1)]) + ' '
    return ans[:-1]

n = int(input())
a = list(map(int,input().split()))
b = collections.deque()
for i in range(n):
    if i%2==0:
        b.append(a[i])
    else:
        b.appendleft(a[i])
print((f(b)))

