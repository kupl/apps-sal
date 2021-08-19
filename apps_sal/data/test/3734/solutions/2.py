def main():
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    try:
        while True:
            a = days.index(input())
            b = days.index(input())
            print('YES' if (b - a) % 7 in (0, 2, 3) else 'NO')
    except EOFError:
        pass


main()
