n=int(input())
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
sum = [0]*n
sum[-1] = a[-1]+b[-1]
for i in range(n-2, -1, -1):
    sum[i] = a[i]+b[i]+sum[i+1]
da = [0]*n
db = [0]*n
da[-1] = b[-1]
db[-1] = a[-1]
for i in range(n-2, -1, -1):
    da[i] = sum[i+1] + da[i+1] + ((n-i)*2-1)*b[i]
    db[i] = sum[i+1] + db[i+1] + ((n-i)*2-1)*a[i]
suml = 0
ans = [0]*n
for i in range(0, n):
    if i%2 == 0:
        ans[i] = suml + da[i] + 2*i*sum[i]
        suml += 2*i*a[i] + (2*i+1)*b[i]
    else:
        ans[i] = suml + db[i] + 2*i*sum[i]
        suml += 2 * i * b[i] + (2 * i + 1) * a[i]
print(max(ans))


