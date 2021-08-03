input_num = int(input())
input_line = input().split()
input_line = [int(s) for s in input_line]
input_line.sort()

if(input_line[int(len(input_line) / 2 - 1)] == input_line[int(len(input_line) / 2)]):
    print((0))
else:
    print((input_line[int(len(input_line) / 2)] - input_line[int(len(input_line) / 2) - 1]))
