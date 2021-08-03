abc = sorted(list(map(int, input().split())), reverse=True)
print((sum(abc) + abc[0] * 9))
