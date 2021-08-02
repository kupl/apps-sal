

def main(k):
    num = list(map(int, k))
    res = []
    while True:
        st = []
        flag = False
        for i in range(len(num)):
            if num[i] > 0:
                st.append('1')
                num[i] -= 1
                flag = True
            else:
                st.append('0')
        if not flag:
            break
        res.append(str(int("".join(st))))
    print(str(len(res)))
    print(" ".join(res))


def __starting_point():
    s = input()
    main(s)


__starting_point()
