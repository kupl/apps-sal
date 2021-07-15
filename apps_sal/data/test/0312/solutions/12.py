n, m = map(int, input().split(' '))
if n == 1:
    print(1)
    return
r = n-m
l = m
print(m-1 if l > r else m+1)
