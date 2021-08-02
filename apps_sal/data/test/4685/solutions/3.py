def ans096(A: int, B: int, C: int, K: int):
    int_list = [A, B, C]
    int_list.sort()
    third = int_list[-1]
    for i in range(K):
        third *= 2
    return int_list[0] + int_list[1] + third


A, B, C = map(int, input().split())
K = int(input())
print(ans096(A, B, C, K))
