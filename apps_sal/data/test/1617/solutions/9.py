n = int(input())
f = []
i = 1
while i*i < n:
    if n%i == 0:
        f.append(i)
        f.append(n//i)
    i += 1
if i*i == n:
    f.append(i)
funs = []
for fs in f:
    funs.append((n*n+2*n-n*fs)//(2*fs))
funs.sort()
print(*funs)

