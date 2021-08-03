A, B, K = map(int, input().split())


def ans120(A: int, B: int, K: int):
    l = sorted([A, B])
    ans_list = []
    for i in range(1, l[1] + 1):
        if A % i == 0 and B % i == 0:
            ans_list.append(i)
    return ans_list[-K]


print(ans120(A, B, K))
