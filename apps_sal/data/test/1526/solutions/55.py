lst = list(map(int, input().split()))
mval = max(lst)
sval = sum(lst)
cn = mval + (sval - mval) % 2
n = (cn * 3 - sval) // 2
print(n)
