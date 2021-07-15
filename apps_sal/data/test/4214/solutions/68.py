import itertools
n = int(input())
a = [list(map(int, input().split(" "))) for i in range(n)]
ans = 0
for [ix,iy], [jx, jy] in itertools.combinations(a, 2):
  ans += ((jx-ix)**2+(jy-iy)**2)**0.5*2
print(ans/n)
