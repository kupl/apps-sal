def R():
    return map(int, input().split())


(n, a, b) = R()
for w in R():
    print(w * a % b // a, end=' ')
