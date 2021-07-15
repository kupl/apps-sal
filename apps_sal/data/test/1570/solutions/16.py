k,n,w = (int(x) for x in input().split())
s = (k + w * k) * w // 2
res = max(0, s - n)
print(res)

