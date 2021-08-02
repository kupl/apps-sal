months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekday1 = input()
weekday2 = input()

days = {
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
    'sunday': 6
}


def main():
    for mon in months[:-1]:
        if (mon + days[weekday1]) % 7 == days[weekday2]:
            print("YES")
            return
    print("NO")
    return


main()
