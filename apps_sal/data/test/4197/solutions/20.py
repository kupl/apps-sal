# -*-coding:utf-8-*-
import sys
input = sys.stdin.readline


def main():
    attended_people = []
    sorted_attended_people = []
    index_number = []
    answer = []
    n = int(input())
    attended_people = list(map(int, input().split()))
    index_number = [[idx, number] for idx, number in enumerate(attended_people)]
    sorted_attended_people = sorted(index_number, key=lambda x: x[1])
    for idx, data in sorted_attended_people:
        answer.append(str(idx + 1))
    print(" ".join(answer))


def __starting_point():
    main()


__starting_point()
