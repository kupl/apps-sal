N = int(input())
(S, T) = list(map(str, input().split()))


def ans148(N: int, S: str, T: str):
    newstr = ''
    for i in range(0, N):
        newstr = newstr + S[i] + T[i]
    return newstr


print(ans148(N, S, T))
