m = list(map(int, input().split()))
w = list(map(int, input().split()))
h = [500, 1000, 1500, 2000, 2500]
s, u = list(map(int, input().split()))
su = 0.0
for i in range(5):
    su += max(0.3*h[i], (1.0-m[i]/250.0)*h[i] - 50.0*w[i])
su += s*100.0
su -= u*50.0
print(int(su))

