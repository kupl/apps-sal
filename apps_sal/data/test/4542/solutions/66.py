from itertools import groupby


# RUN LENGTH ENCODING str -> tuple
def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, str(len(list(v)))))
    return res


# RUN LENGTH DECODING tuple -> str
def runLengthDecode(L: "list[tuple]"):
    res = ""
    for c, n in L:
        res += c * int(n)
    return res


# RUN LENGTH ENCODING str -> list
def rle_list(S: str):
    grouped = groupby(S)
    res = ""
    for k, v in grouped:
        res += k
    return res


def main():
    ss = input()
    rle = rle_list(ss)
    ans = len(list(rle)) - 1
    print(ans)


def __starting_point():
    main()

__starting_point()
