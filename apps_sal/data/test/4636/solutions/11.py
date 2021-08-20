def solve(n, sizes):
    last = sizes[0]
    result = {'n_steps': 1, 'a': last, 'b': 0}
    flag_a = 1
    flag_b = n - 1
    turn = 'b'
    if flag_a == flag_b + 1:
        return result
    while True:
        cur = 0
        result['n_steps'] += 1
        if flag_a == flag_b + 1:
            return result
        if turn == 'a':
            while cur <= last:
                cur += sizes[flag_a]
                result['a'] += sizes[flag_a]
                flag_a += 1
                if flag_a == flag_b + 1:
                    return result
            last = cur
            turn = 'b'
        else:
            while cur <= last:
                cur += sizes[flag_b]
                result['b'] += sizes[flag_b]
                flag_b -= 1
                if flag_a == flag_b + 1:
                    return result
            last = cur
            turn = 'a'


def main():
    tests = int(input())
    for t in range(tests):
        n = int(input())
        sizes = list(map(int, input().split()))
        result = solve(n, sizes)
        print(result['n_steps'], result['a'], result['b'])


main()
