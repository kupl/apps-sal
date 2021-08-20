def main():
    n = int(input())
    initial_population = 0
    maximum_population = 0
    current_population = 0
    population_snapshots = [0] * (n + 1)
    population_set = set()

    def increase(index):
        if index > 0:
            population_snapshots[index] = population_snapshots[index - 1] + 1
        else:
            population_snapshots[index] = 1

    def copy(index):
        if index > 0:
            population_snapshots[index] = population_snapshots[index - 1]
        else:
            population_snapshots[index] = 0

    def decrease(index):
        population_snapshots[index] = population_snapshots[index - 1] - 1

    def increment_upto(end):
        for i in range(end + 1):
            population_snapshots[i] += 1
    for index in range(1, n + 1):
        (direction, receipt) = input().split()
        if direction == '+':
            increase(index)
            current_population += 1
            population_set.add(receipt)
        elif receipt in population_set:
            decrease(index)
            current_population -= 1
            population_set.remove(receipt)
        else:
            copy(index)
            increment_upto(index - 1)
            initial_population += 1
        maximum_population = max(maximum_population, current_population)
    print(max(population_snapshots))


def __starting_point():
    main()


__starting_point()
