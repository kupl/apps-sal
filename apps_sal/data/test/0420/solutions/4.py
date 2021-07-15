from sys import stdin

def isreversed(a):
    if(len(a) % 2 == 0):
        if(a[:len(a) // 2] == a[len(a) // 2:][::-1]):
            return True
    return False

a = []
n, m = list(map(int, stdin.readline().split()))
for i in range(n):
    a.append(list(map(int, stdin.readline().split())))
res = n
while(isreversed(a)):
    res //= 2
    a = a[:len(a) // 2]
print(res)
