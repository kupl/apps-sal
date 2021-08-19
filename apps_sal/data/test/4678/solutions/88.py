class Person:

    def __init__(self, num, height):
        self.num = num
        self.height = height

    @staticmethod
    def static():
        print('static')


def main():
    number = int(input())
    person_list = list(map(int, input().split()))
    ans = 0
    for (num, person) in enumerate(person_list):
        if num > 0:
            if person < person_list[num - 1]:
                person_list[num] = person_list[num - 1]
                ans += person_list[num - 1] - person
    print(ans)


def __starting_point():
    main()


__starting_point()
