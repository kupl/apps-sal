import sys
n = int(sys.stdin.readline().strip())
integer_line = sys.stdin.readline().strip().split()
integers = []
for integer in integer_line:
    integers.append(int(integer))

marks = integers[:]
marks[0] = 1
for index in range(1, len(integers)):
    marks[index] = max(marks[index - 1], marks[index] + 1)
for index in range(len(integers) - 1, 0, -1):
    marks[index - 1] = max(marks[index] - 1, marks[index - 1])
for index in range(len(integers)):
    marks[index] -= integers[index] + 1
sys.stdout.write(str(sum(marks)) + "\n")
