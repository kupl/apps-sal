def ri(): return int(input())
def rli(): return list(map(int, input().split()))
def rls(): return list(input())
def pli(a): return "".join(list(map(str, a)))


n, a = rli()
minang = 180/n
v1 = 2
v2 = 1
minerr = 114514810
v3 = 0
for i in range(3, n+1):
    if(minerr > abs(a-minang*(i-2))):
        v3 = i
        minerr = abs(a-minang*(i-2))

print(v1, v2, v3)
