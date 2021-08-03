N, K = map(int, input().split())
bl = set(input().split())

while True:
    if len(set(str(N)) & bl) != 0:
        N += 1
    else:
        print(N)
        break
