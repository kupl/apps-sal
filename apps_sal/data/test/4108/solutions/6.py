s = input()
t = input()
ds = {}
dt = {}
ans = 'Yes'
for (S, T) in zip(s, t):
    if S in ds:
        if ds[S] != T:
            ans = 'No'
            break
    else:
        ds[S] = T
    if T in dt:
        if dt[T] != S:
            ans = 'No'
            break
    else:
        dt[T] = S
print(ans)
