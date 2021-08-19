def solve(k, bits):
    indices = []
    for (i, b) in enumerate(bits):
        if b == '0':
            indices.append(i)
    cur = k
    for i in range(len(indices)):
        index = indices[i]
        move = index - i
        if move > cur:
            indices[i] = index - cur
            break
        else:
            indices[i] = i
            cur -= move
    ans = ['1'] * len(bits)
    for index in indices:
        ans[index] = '0'
    return ''.join(ans)


def __starting_point():
    q = int(input())
    for _ in range(q):
        (n, k) = [int(r) for r in input().split(' ')]
        print(solve(k, input()))


__starting_point()
