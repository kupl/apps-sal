def main():
    line = input()
    array = []
    count = 0
    even = 0
    for char in line:
        if array == [] or array[-1] == char:
            array.append(char)
            count += 1
        else:
            array.append(char)
            if count % 2 == 0:
                even += 1
            count = 1
    if count % 2 == 0:
        even += 1
    print(even)


main()
