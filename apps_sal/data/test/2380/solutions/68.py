import heapq


def main():
    N, M = list(map(int, input().split()))
    n_list = list(map(int, input().split()))
    n_dic = {}
    for n in n_list:
        n_dic.setdefault(n, 0)
        n_dic[n] += 1

    for i in range(M):
        b, c = list(map(int, input().split()))
        n_dic.setdefault(c, 0)
        n_dic[c] += b

    com_list = []

    for score, num in list(n_dic.items()):
        heapq.heappush(com_list, (-score, num))

    taken = 0
    result = 0

    while True:
        score, num = heapq.heappop(com_list)
        score = -score
        if N - taken > num:
            result += score * num
            taken += num
        else:
            result += score * (N - taken)
            break

    print(result)


main()
