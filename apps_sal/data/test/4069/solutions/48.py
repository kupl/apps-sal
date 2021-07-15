X, K, D = map(int, input().split())


X = abs(X)
a = K*D
if X >= a:
    result = X-a
else:
    b = X//D
    c = (X-b*D)
    d = abs(X-(b+1)*D)
    if c < d:
        if b%2==K%2:
            result = c
        else:
            result = d
    else:
        if (b+1)%2==K%2:
            result=d
        else:
            result=c

print(result)
