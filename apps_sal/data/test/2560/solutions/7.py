for i in range(int(input())):

    n, l, r = list(map(int, input().split()))

    print('No' if (n // l) * r < n else 'Yes')


# Made By Mostafa_Khaled
