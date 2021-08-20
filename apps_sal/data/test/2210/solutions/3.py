T = int(input())
for _ in range(T):
    (N, s) = map(int, input().split())
    s -= 1
    X = [[] for _ in range(N)]
    for i in range(N - 1):
        (a, b) = map(int, input().split())
        (a, b) = (a - 1, b - 1)
        X[a].append(b)
        X[b].append(a)
    if len(X[s]) <= 1:
        print('Ayush')
        continue
    if (N - 3) % 2:
        print('Ayush')
    else:
        print('Ashish')
