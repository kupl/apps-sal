def is_dislike(N, ds):
    num = N
    while True:
        if num % 10 in ds:
            return True
        else:
            num = int(num / 10)
            if num == 0:
                break
    return False


nk = list(map(int, input().split()))
N = nk[0]
K = nk[1]
ds = list(map(int, input().split()))
while True:
    if is_dislike(N, ds):
        N = N + 1
    else:
        print(N)
        break
