name = input()
text = input()


def fun():
    first_end = len(text)
    last_start = 0
    current_index = 0
    for i in range(len(text)):
        if text[i] == name[current_index]:
            current_index += 1
            if current_index == len(name):
                first_end = i
                break
    current_index = len(name) - 1
    for i in range(len(text) - 1, first_end, -1):
        if text[i] == name[current_index]:
            current_index -= 1
            if current_index == -1:
                last_start = i
                break
    diff = last_start - first_end
    if diff < 1:
        print('0')
    else:
        print(diff)


fun()

