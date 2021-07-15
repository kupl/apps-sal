n = int(input())
f = [1]
for i in range(1, 21):
    f.append(f[-1]*i)
print((f[n]*f[n//2 - 1]**2)//(2*f[n//2]**2))

