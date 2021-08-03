n = int(input())
x = list(map(int, input().split()))
ans = []
if len(set(x)) == 1:
    print(0)
else:
    for p in range(min(x), max(x)):
        meter = 0
        for xi in x:
            meter += pow((xi - p), 2)
        ans.append(meter)
    print(min(ans))
