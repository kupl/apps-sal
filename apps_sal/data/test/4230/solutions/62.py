(X, N) = map(int, input().split())
p = list(map(int, input().split()))
count = -1
while True:
    count += 1
    if X - count not in p:
        print(X - count)
        break
    elif X + count not in p:
        print(X + count)
        break
