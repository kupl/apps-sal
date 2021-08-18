from itertools import permutations

MOD = 10**9 + 7


def main():
    n = int(input())
    parent = [0] * n
    is_leaf = [True] * n
    for i in range(1, n):
        parent[i] = int(input()) - 1
        is_leaf[parent[i]] = False
    leafs_cnt = [0] * n
    for i in range(n):
        leafs_cnt[parent[i]] += is_leaf[i]
    for i in range(n):
        if not is_leaf[i] and leafs_cnt[i] < 3:
            print("No")
            return
    print("Yes")


while 1:
    main()
    break
