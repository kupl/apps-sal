a = input()
N = int(a)
d = list(map(int,input().split()))

d.sort()
print((d[N//2]-d[N//2-1]))

