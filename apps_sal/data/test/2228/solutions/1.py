def findMaxGuests(arrl, exit, n):
    arrl.sort()
    exit.sort()

    guests_in = 1
    max_guests = 1
    time = arrl[0]
    i = 1
    j = 0

    while (i < n and j < n):

        if (arrl[i] <= exit[j]):

            guests_in = guests_in + 1

            if (guests_in > max_guests):
                max_guests = guests_in
                time = arrl[i]

            i = i + 1

        else:
            guests_in = guests_in - 1
            j = j + 1

    print(time, max_guests)


t = int(input())
arrl = []
exit = []
for _ in range(t):
    a, b = list(map(int, input().strip().split(" ")))
    arrl.append(a)
    exit.append(b - 1)
n = len(arrl)
findMaxGuests(arrl, exit, n)
