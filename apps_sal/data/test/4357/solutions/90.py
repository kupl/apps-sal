abc = sorted(list(map(int, input().split())), reverse=True)
a = [1] * 10
for i in range(10 ** 7 + 5 * 10 ** 6):
    a.append(a)
print(sum(abc) + abc[0] * 9)
