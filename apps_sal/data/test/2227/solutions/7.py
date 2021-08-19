#!/usr/bin/env python3

def main():
    line = input()
    final = 0
    count = 0
    for i in range(len(line) - 4):
        if 'heavy' == line[i:i + 5]:
            count += 1
            i += 5
        elif 'metal' == line[i:i + 5]:
            final += count
            i += 5
    print(final)


def __starting_point():
    main()


__starting_point()
