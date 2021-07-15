n = int(input())
#a, b = map(int,input().split())
al = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

total = sum(al)
mn = abs(total-2*al[0])
x = 0
for i in range(1, n-1):
    x += al[i-1]
    y = total-x
    mn = min(mn, abs(x-y))

print(mn)

