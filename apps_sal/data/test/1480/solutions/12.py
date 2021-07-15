from copy import deepcopy as dcopy
def main():
    n, k = list(map(int, input().split()))
    ks = list(map(int, input().split()))

    children = list(range(n))
    leader_i = 0
    res = []
    for k in ks:
        elim_i = (leader_i + k) % len(children)
        elim_num = dcopy(children[elim_i])
        nextl_i = (leader_i + k + 1) % len(children)
        nextl_num = dcopy(children[nextl_i])
        res.append(children.pop(elim_i)+1)
        leader_i = children.index(nextl_num)

    print(' '.join(map(str,res)))

def __starting_point():
    main()

__starting_point()
