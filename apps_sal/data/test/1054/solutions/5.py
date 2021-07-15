#!/usr/bin/env python3

number_of_mines = int(input())
x_coords = []
y_coords = []
for _ in range(number_of_mines):
    x, y = (int(value) for value in input().split())
    x_coords.append(x)
    y_coords.append(y)
print(max(abs(max(x_coords) - min(x_coords)), abs(max(y_coords) - min(y_coords))) ** 2)
    


