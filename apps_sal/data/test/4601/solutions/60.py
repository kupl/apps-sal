N, K = map(int, input().split())
H = input()


def ans153(N: int, K: int, H: str):
    if K == 0:
        H_list = sorted(list(map(int, H.split())))
        return sum(H_list)
    elif len(list(map(int, H.split()))) > K:
        H_list = sorted(list(map(int, H.split())))
        H_list = H_list[:-K]
        return sum(H_list)
    else:
        return 0


print(ans153(N, K, H))
