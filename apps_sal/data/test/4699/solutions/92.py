(N, K) = list(map(int, input().split()))
kirai = list(map(int, input().split()))
while True:
    bara = [int(x) for x in list(str(N))]
    diff = set(kirai) & set(bara)
    if diff == set():
        print(N)
        break
    else:
        N = N + 1
