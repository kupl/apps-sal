def main():
    _ = int(input())
    s = input()

    st = []
    for c in s:
        if c == 'x':
            if len(st) >= 2 and st[-1] == 'o' and st[-2] == 'f':
                for _ in range(2):
                    st.pop()
                continue
        st.append(c)
    ans = len(st)
    print(ans)


def __starting_point():
    main()


__starting_point()
