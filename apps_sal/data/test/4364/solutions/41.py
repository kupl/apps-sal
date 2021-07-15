import re


def answer(s: str) -> str:
    YYMM = r'^[0-9]{2}(0[1-9]|1[0-2])$'
    MMYY = r'^(0[1-9]|1[0-2])[0-9]{2}$'
    YYMM_result = re.match(YYMM, s)
    MMYY_result = re.match(MMYY, s)

    if YYMM_result and MMYY_result:
        return 'AMBIGUOUS'
    if YYMM_result:
        return 'YYMM'
    if MMYY_result:
        return 'MMYY'
    return 'NA'


def main():
    s = input()
    print((answer(s)))


def __starting_point():
    main()

__starting_point()
