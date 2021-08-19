#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import array


def z_sorted(length, sequence):
    sorted_sequence = sorted(sequence)
    answer = []
    for i in range(length // 2):
        answer.append(sorted_sequence[i])
        answer.append(sorted_sequence[length - i - 1])
    if length % 2 == 1:
        answer.append(sorted_sequence[length // 2])
    return answer


def main():
    length = int(input())
    sequence = array.array("L", list(map(int, input().split())))
    print(" ".join(map(str, z_sorted(length, sequence))))


def __starting_point():
    main()


__starting_point()
