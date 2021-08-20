a = list(map(int, input().split()))
b = set(a)
for i in b:
    if a.count(i) == 1:
        print(i)
