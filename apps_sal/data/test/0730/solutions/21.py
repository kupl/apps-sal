k = int(input())
print('+------------------------+')
a = (k - 4) // 3
b = (k - 4) % 3
if k == 0:
    print('|#.#.#.#.#.#.#.#.#.#.#.|D|)')
    print('|#.#.#.#.#.#.#.#.#.#.#.|.|')
    print('|#.......................|')
    print('|#.#.#.#.#.#.#.#.#.#.#.|.|)')
elif k == 1:
    print('|O.#.#.#.#.#.#.#.#.#.#.|D|)')
    print('|#.#.#.#.#.#.#.#.#.#.#.|.|')
    print('|#.......................|')
    print('|#.#.#.#.#.#.#.#.#.#.#.|.|)')
elif k == 2:
    print('|O.#.#.#.#.#.#.#.#.#.#.|D|)')
    print('|O.#.#.#.#.#.#.#.#.#.#.|.|')
    print('|#.......................|')
    print('|#.#.#.#.#.#.#.#.#.#.#.|.|)')
elif k == 3:
    print('|O.#.#.#.#.#.#.#.#.#.#.|D|)')
    print('|O.#.#.#.#.#.#.#.#.#.#.|.|')
    print('|O.......................|')
    print('|#.#.#.#.#.#.#.#.#.#.#.|.|)')
elif k == 4:
    print('|O.#.#.#.#.#.#.#.#.#.#.|D|)')
    print('|O.#.#.#.#.#.#.#.#.#.#.|.|')
    print('|O.......................|')
    print('|O.#.#.#.#.#.#.#.#.#.#.|.|)')
elif b == 0:
    print('|O' + '.O' * a + '.#' * (10 - a) + '.|D|)')
    print('|O' + '.O' * a + '.#' * (10 - a) + '.|.|')
    print('|O.......................|')
    print('|O' + '.O' * a + '.#' * (10 - a) + '.|.|)')
elif b == 1:
    print('|O' + '.O' * (a + 1) + '.#' * (10 - a - 1) + '.|D|)')
    print('|O' + '.O' * a + '.#' * (10 - a) + '.|.|')
    print('|O.......................|')
    print('|O' + '.O' * a + '.#' * (10 - a) + '.|.|)')
elif b == 2:
    print('|O' + '.O' * (a + 1) + '.#' * (10 - a - 1) + '.|D|)')
    print('|O' + '.O' * (a + 1) + '.#' * (10 - a - 1) + '.|.|')
    print('|O.......................|')
    print('|O' + '.O' * a + '.#' * (10 - a) + '.|.|)')
print('+------------------------+')
