a_line = input()
a_line = list(a_line)
# print(a_line)
b_line = input()
b_line = list(b_line)

c_line = input()
c_line = list(c_line)

end = 0
turn = "a"

while(end == 0):
    if turn == "a":
        if len(a_line) == 0:
            end = "A"
        else:
            temp = a_line[0]
            del a_line[0]
            # print(a_line)
            turn = temp

    elif turn == "b":
        if len(b_line) == 0:
            end = "B"
        else:
            temp = b_line[0]
            del b_line[0]
            # print(b_line)
            turn = temp

    else:
        if len(c_line) == 0:
            end = "C"
        else:
            temp = c_line[0]
            del c_line[0]
            # print(b_line)
            turn = temp


print(end)
