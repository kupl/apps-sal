n = int(input())

trips = []

prix = [0]

k = 0

j = 0

for i in range(n):

    trips.append(int(input()))

    while trips[i] - trips[j] >= 90:

        j += 1

    while trips[i] - trips[k] >= 1440:

        k += 1

    prix.append(min(min(prix[k] + 120, prix[j] + 50), prix[-1] + 20))

    print(prix[-1] - prix[-2])


# Made By Mostafa_Khaled
