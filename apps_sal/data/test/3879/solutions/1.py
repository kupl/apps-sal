def solve(N, As):
    core = find_core(As[0])
    for a in As[1:]:
        core_a = find_core(a)
        if core != core_a:
            return False
    return True


def find_core(a):
    while a % 2 == 0:
        a //= 2
    while a % 3 == 0:
        a //= 3
    return a


N = int(input())
As = list(map(int, input().split()))
if solve(N, As):
    print('Yes')
else:
    print('No')
