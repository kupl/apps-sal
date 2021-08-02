def handle_string(string):
    new_string = ''
    for i in range(len(string)):
        if string[i] == 'B':
            if len(new_string) != 0:
                new_string = new_string[0:len(new_string) - 1]
            else:
                continue
        else:
            new_string = new_string + string[i]
    return new_string


input_string = input()
print(handle_string(input_string))
