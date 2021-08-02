__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    lights = []
    results = [['', '', ''], ['', '', ''], ['', '', '']]

    for _ in range(3):
        lights.append([int(word) for word in input().split()])

    for i in range(3):
        for j in range(3):
            temp = lights[i][j] \
                + (lights[i - 1][j] if i > 0 else 0) \
                + (lights[i][j - 1] if j > 0 else 0) \
                + (lights[i + 1][j] if i < 2 else 0) \
                + (lights[i][j + 1] if j < 2 else 0)
            results[i][j] = str(1 - temp % 2)

    result_strings = [''.join(listi) for listi in results]
    print('\n'.join(result_strings))

    return 0


def __starting_point():
    exit(main())


__starting_point()
