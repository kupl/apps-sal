def abc(d, down_text, up_text):
    d[down_text] -= 1
    d[up_text] += 1


def main():
    (n, a, b, c) = map(int, input().split())
    ans_list = []
    dct = {'A': a, 'B': b, 'C': c}
    abc_list = [input() for _ in range(n)]
    abc_list.append('AB')
    for i in range(n):
        l_txt = abc_list[i][0]
        r_txt = abc_list[i][1]
        if dct[l_txt] < dct[r_txt]:
            abc(dct, r_txt, l_txt)
            ans_list.append(l_txt)
        elif dct[l_txt] > dct[r_txt]:
            abc(dct, l_txt, r_txt)
            ans_list.append(r_txt)
        elif dct[l_txt] == dct[r_txt] == 0:
            print('No')
            break
        elif l_txt in abc_list[i + 1]:
            abc(dct, r_txt, l_txt)
            ans_list.append(l_txt)
        elif r_txt in abc_list[i + 1]:
            abc(dct, l_txt, r_txt)
            ans_list.append(r_txt)
    else:
        print('Yes')
        print(*ans_list, sep='\n')


def __starting_point():
    main()


__starting_point()
