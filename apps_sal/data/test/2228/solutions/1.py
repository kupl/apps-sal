# Program to find maximum guest
# at any time in a party
def findMaxGuests(arrl, exit, n):
    # Sort arrival and exit arrays
    arrl.sort()
    exit.sort()

    # guests_in indicates number of
    # guests at a time
    guests_in = 1
    max_guests = 1
    time = arrl[0]
    i = 1
    j = 0

    # Similar to merge in merge sort to
    # process all events in sorted order
    while (i < n and j < n):

        # If next event in sorted order is
        # arrival, increment count of guests
        if (arrl[i] <= exit[j]):

            guests_in = guests_in + 1

            # Update max_guests if needed
            if (guests_in > max_guests):
                max_guests = guests_in
                time = arrl[i]

            # increment index of arrival array
            i = i + 1

        else:
            guests_in = guests_in - 1
            j = j + 1

    print(time, max_guests)


# Driver Code
t = int(input())
arrl = []
exit = []
for _ in range(t):
    a, b = list(map(int, input().strip().split(" ")))
    arrl.append(a)
    exit.append(b - 1)
n = len(arrl)
findMaxGuests(arrl, exit, n)

# This code is contributed
# by Shivi_Aggarwal
