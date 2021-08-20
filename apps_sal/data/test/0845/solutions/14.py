def main():
    keys = 'qwertyuiopasdfghjkl;zxcvbnm,./'
    direction = input()
    message = input()
    if direction == 'L':
        offset = 1
    else:
        offset = -1
    for letter in message:
        print(keys[keys.index(letter) + offset], end='')


main()
