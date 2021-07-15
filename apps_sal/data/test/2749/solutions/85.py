def main():
    def flatten_list(l):
        for el in l:
            if isinstance(el, list):
                yield from flatten_list(el)
            else:
                yield el
    H, W = list(map(int, input().split()))
    n = int(input())
    A = list(map(int, input().split()))
    ans = []
    for i, a in enumerate(A):
        ans .append([str(i + 1)] * a)
    ans = list(flatten_list(ans))
    ans = [ans[i:i + W] if i // W % 2 == 0 else ans[i + W - 1:i - 1:-1] for i in range(0, len(ans), W)]
    [print(' '.join(a)) for a in ans]

def __starting_point():
    main()

__starting_point()
