def main():
    read = lambda: tuple(map(int, input().split()))
    n = read()[0]
    state = [1, 1, 0]
    def f(x, state):
        for i in range(3):
            if i != x:
                state[i] = 1 - state[i]
    #print(n, state)
    for i in range(n):
        c = read()[0] - 1
        if state[c] == 0:
            return "NO"
        f(c, state)
    return "YES"
print(main())

