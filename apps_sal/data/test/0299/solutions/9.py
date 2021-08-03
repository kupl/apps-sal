def main() -> int:
    n = int(input())
    exercises = [int(word) for word in input().split()]
    total = [0] * 3

    for i in range(3):
        total[i] = sum(exercises[i::3])

    max_index = total.index(max(total))
    exercise_names = ['chest', 'biceps', 'back']

    print(exercise_names[max_index])

    return 0


def __starting_point():
    main()


__starting_point()
