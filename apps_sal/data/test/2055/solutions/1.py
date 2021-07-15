def main():
    for case in range(int(input())):
        n = int(input().strip())
        as_ = [int(t) for t in input().strip().split()]
        bs = [int(t) for t in input().strip().split()]
        
        print(solve(as_=as_, bs=bs))


def solve(as_, bs):
    if get_update_dir(as_, bs, 0) == 0:
        return 'YES'

    lt = 0
    gt = as_[0] + 1

    while gt > lt + 1:
        mid = (lt + gt) // 2
        
        update_dir = get_update_dir(as_, bs, mid)

        if update_dir == 0:
            return 'YES'

        if update_dir > 0:
            lt = mid
        else:
            gt = mid

    return 'NO'


def get_update_dir(as_, bs, x):
    if x > as_[0] or x > bs[-1]:
        return -1

    if x < 0:
        return +1

    left = x
    for a, b in zip(as_, bs):
        right = a - min(left, a)

        if right > b:
            return +1
        
        left = b - right

    if right + x > bs[-1]:
        return -1

    return 0


main()

