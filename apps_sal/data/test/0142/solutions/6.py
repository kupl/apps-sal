
def main():
    n, needed = list(map(int, input().split()))
    costs = list(map(int, input().split()))

    done = False
    while not done:
        done = True
        cur = costs[0]
        for i, x in enumerate(costs[1:], 1):
            cur <<= 1
            if cur < x:
                costs[i] = cur
                done = False
            else:
                cur = x
        for i in range(n - 2, -1, -1):
            if costs[i] > costs[i + 1]:
                costs[i] = costs[i + 1]
                done = False

    def calc(total):
        result = 0
        for i in range(31):
            if total & 1 << i:
                if i < n:
                    result += costs[i]
                else:
                    result += costs[-1] << (i - n + 1)
        return result

    result = calc(needed)
    for i in range(30, -1, -1):
        x = (needed >> i | 0x1) << i
        if x >= needed:
            result = min(result, calc(x))

    print(result)


try:
    while True:
        main()
except EOFError:
    pass
