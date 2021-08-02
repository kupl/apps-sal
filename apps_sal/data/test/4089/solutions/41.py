# coding=utf-8

def __starting_point():
    N = int(input())
    N -= 1
    ans = []

    while True:
        if N >= 26:
            ans.insert(0, N % 26)
            N = N // 26 - 1

        else:
            ans.insert(0, N)
            break

    # print(ans)

    def num2alpha(c): return chr(c + 97)
    for i in range(len(ans)):
        print(num2alpha(ans[i]), end='')


__starting_point()
