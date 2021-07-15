n,m = list(map(int, input().split()))

xp_yp_zp = [0] * n
xp_yp_zn = [0] * n
xp_yn_zp = [0] * n
xn_yp_zp = [0] * n
xp_yn_zn = [0] * n
xn_yp_zn = [0] * n
xn_yn_zp = [0] * n
xn_yn_zn = [0] * n

for i in range(n):
  x,y,z = list(map(int, input().split()))
  xp_yp_zp[i] = x + y + z
  xp_yp_zn[i] = x + y - z
  xp_yn_zp[i] = x - y + z
  xn_yp_zp[i] = -x + y + z
  xp_yn_zn[i] = x - y - z
  xn_yp_zn[i] = -x + y - z
  xn_yn_zp[i] = -x - y + z
  xn_yn_zn[i] = -x - y - z

xp_yp_zp.sort(reverse = True)
a = sum(xp_yp_zp[0:m])

xp_yp_zn.sort(reverse = True)
b = sum(xp_yp_zn[0:m])

xp_yn_zp.sort(reverse = True)
c = sum(xp_yn_zp[0:m])

xn_yp_zp.sort(reverse = True)
d = sum(xn_yp_zp[0:m])

xp_yn_zn.sort(reverse = True)
e = sum(xp_yn_zn[0:m])

xn_yp_zn.sort(reverse = True)
f = sum(xn_yp_zn[0:m])

xn_yn_zp.sort(reverse = True)
g = sum(xn_yn_zp[0:m])

xn_yn_zn.sort(reverse = True)
h = sum(xn_yn_zn[0:m])

ans = max(a,b,c,d,e,f,g,h)

print(ans)

