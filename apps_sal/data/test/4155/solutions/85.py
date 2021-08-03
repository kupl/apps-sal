
url = "https://atcoder.jp//contests/abc116/tasks/abc116_c"


def main():
    input()
    h = list(map(int, input().split()))
    h.append(0)
    count = 0

    def start_end(h):
        s_e = [-1, -1]
        for i in range(len(h)):
            if h[i] != 0 and s_e[0] == -1:
                s_e[0] = i
            elif h[i] == 0 and s_e[0] != -1:
                s_e[1] = i
                break
        return s_e
    while True:
        s_e = start_end(h)
        if s_e[0] == -1 and s_e[1] == -1:
            print(count)
            return
        min_h = min(h[s_e[0]:s_e[1]])
        for i in range(s_e[0], s_e[1]):
            h[i] -= min_h
        count += min_h


def __starting_point():
    main()


__starting_point()
