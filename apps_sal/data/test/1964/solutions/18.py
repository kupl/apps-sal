def calculator(men, buying):
    result = 0
    result += sum(buying) * 5
    result += men * 15
    return result


def main():
    pay_desks = int(input())
    queue = list(map(int, input().split()))
    temporal = 0
    amount = calculator(queue[0], list(map(int, input().split())))
    for i in range(1, pay_desks):
        temporal = calculator(queue[i], list(map(int, input().split())))
        if temporal < amount:
            amount = temporal
    print(amount)


main()
