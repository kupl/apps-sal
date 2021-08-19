(N, K) = map(int, input().split())
D = set(input().split())
for i in range(N, 100001):
    for d in str(i):
        if d in D:
            break
    else:
        print(i)
        break
