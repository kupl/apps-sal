def Next(): return input()
def NextInt(): return int(Next())
def NextInts(): return map(int,input().split())
def Nexts(): return map(str,input().split())
def NextIntList(): return list(map(int,input().split()))
def RowInts(n): return [input() for i in range(n)]

def output(ans):
    print("Yes")
    size = len(ans)
    for i in range(size):
        if i == size-1:
            print(ans[i])
        else:
            print(ans[i], end=' ')

n = NextInt()
a = NextIntList()
b = NextIntList()[::-1]


def solve():
    border = n-1
    for i in range(n):
        if(a[i] >= b[i]):
            border = i
            break
    if a[border] != b[border]:
        output(b)
        return
    key = a[border]
    if a.count(key)+b.count(key) > n:
        print("No")
        return
    cnt = a[:border].count(key) + b[:border].count(key)

    for i in range(border, n):
        if a[i] != key or b[i] != key:
            output(b[i-1::-1] + b[:i-1:-1])
            return
        cnt += 2
        if cnt == i+1:
            output(b[i::-1] + b[:i:-1])
            return
    output(b[::-1])

solve()
