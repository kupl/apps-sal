def main():
    import sys
    tokens = [int(i) for i in sys.stdin.read().split()]
    tokens.reverse()
    (n, l, x, y) = [tokens.pop() for i in range(4)]
    marks = set(tokens)
    x_index = y_index = sum_index = sub_index1 = sub_index2 = -1
    for i in marks:
        if i + x in marks:
            x_index = y
        if i + y in marks:
            y_index = x
        if i + x + y in marks:
            sum_index = i + x
        if i + y - x in marks and i - x >= 0:
            sub_index1 = i - x
        if i + y - x in marks and i + y <= l:
            sub_index2 = i + y
    if x_index != -1 and y_index != -1:
        print(0)
    else:
        for i in (x_index, y_index, sum_index, sub_index1, sub_index2):
            if i != -1:
                print(1)
                print(i)
                break
        else:
            print(2)
            print(x, y)


main()
