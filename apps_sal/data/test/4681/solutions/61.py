n = int(input())
l = [2, 1]
if n == 0:
    print(2)
elif n == 1:
    print(1)
else:
    for i in range(n - 1):
        l.append(l[-1] + l[-2])
    print(l[-1])
