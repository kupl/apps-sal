#!/usr/local/bin/python3

input()

binary_number = input()

splitted = binary_number.split('0')
digits = list(map(len, splitted))
print(''.join(map(str, digits)))
