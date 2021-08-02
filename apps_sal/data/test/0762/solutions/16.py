def main():
    n, b = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    values = []
    count = 0
    last_item = 0
    start = False
    for item in numbers:
        if start and count == 0:
            values += [abs(item - last_item)]

        if item % 2 == 0:
            count += 1
        else:
            count -= 1

        last_item = item
        start = True

    answer = 0
    answer_count = 0
    for value in sorted(values):
        if answer + value <= b:
            answer += value
            answer_count += 1

    print(answer_count)


main()
