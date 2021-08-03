N = int(input())
d = [input() for i in range(N)]


def ans085(N: int, d: str):
    d = map(int, d)
    return(len(set(d)))


print(ans085(N, d))
