
def resolve():
    N, K, C = list(map(int, input().split()))
    S = input()

    left = [0]*N
    i = 0
    cnt = 1
    while i < N:
        if S[i] == "o":
            left[i] = cnt
            i += C
            cnt += 1
        i += 1

    right = [0]*N
    i = 0
    cnt = K
    T = S[::-1]
    while i < N:
        if T[i] == "o":
            right[i] = cnt
            i += C
            cnt -= 1
        i += 1
    right = right[::-1]

    for i in range(N):
        if left[i] == 0:
            continue
        if left[i] == right[i]:
            print((i+1))

def __starting_point():
    resolve()

__starting_point()
