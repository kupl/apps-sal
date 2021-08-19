def gi():
    return list(map(int, input().split()))


(n,) = gi()
l = gi()
print(max(l) - min(l) + 1 - len(l))
