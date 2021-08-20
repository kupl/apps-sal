import numpy as np
import sys
input = sys.stdin.readline


def main():
    restaurants = []
    n = int(input())
    restaurants = [list(input().split()) for _ in range(n)]
    for (idx, restaurant) in enumerate(restaurants):
        restaurants[idx][1] = int(str(restaurant[1]))
        restaurants[idx].append(idx + 1)
    restaurants.sort(key=lambda x: x[1], reverse=True)
    restaurants.sort(key=lambda x: x[0].lower())
    for restaurant in restaurants:
        print(restaurant[2])


def __starting_point():
    main()


__starting_point()
