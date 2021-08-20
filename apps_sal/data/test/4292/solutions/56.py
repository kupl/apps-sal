def I():
    return map(int, input().split())


(_, k) = I()
print(sum(sorted(I())[:k]))
