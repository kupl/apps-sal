abc = sorted(list(map(int, input().split())), reverse=True)
a = [1] * 10
for i in range(10**7):
    a.append(a)
print((sum(abc) + abc[0] * 9))
