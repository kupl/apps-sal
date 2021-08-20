a = int(input())
xy = [map(int, input().split()) for _ in range(a)]
(x, y) = [list(i) for i in zip(*xy)]
f = 0
for i in range(len(x)):
    if x[i] == y[i] and len(x) > i + 2:
        for j in range(1, 3):
            if x[i + j] != y[i + j]:
                break
        else:
            print('Yes')
            break
else:
    print('No')
