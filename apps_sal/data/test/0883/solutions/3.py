import sys
my_file = sys.stdin
#my_file = open("input.txt", "r")
friends = int(my_file.readline().strip("\n")) + 1
fingers = sum([int(i) for i in my_file.readline().split(" ")])
result = 0
for i in range(1, 6):
    if (i + fingers) % friends != 1:
        result += 1
print(result)
