(n, h) = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
answer = 0
for i in range(1, n + 1):
    a = c[:i]
    a.sort(reverse=True)
    summa = 0
    for item in range(0, i, 2):
        summa += a[item]
    if summa > h:
        print(answer)
        break
    else:
        answer = i
else:
    print(answer)
