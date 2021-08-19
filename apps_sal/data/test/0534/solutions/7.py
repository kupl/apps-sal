import math
import sys
# Main function


def cantina():
    datain = []
    queue = []

    # Taking input
    for i in range(2):
        datain.append(input().split())

    # Setting time in
    time = int(datain[0][1])

    # Making queue list
    for i in range(len(datain[1][0])):
        queue.append(datain[1][0][i])

    # Queueswaps based on amount of times
    for i in range(time):
        queueswap(queue)

    # returns queue
    return queue

# Function for swapping


def queueswap(queue):
    swaps = []

    # Finds places to swap
    for i in range(len(queue) - 1):
        if queue[i] == "B" and queue[i + 1] == "G":
            swaps.append(i)

    # Swaps the places
    for i in swaps:
        queue[i] = "G"
        queue[i + 1] = "B"

    # returns the corrected list
    return queue


# Prints the output string
print(''.join(cantina()))
