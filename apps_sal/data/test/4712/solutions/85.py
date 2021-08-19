# coding: utf-8

height, width = map(int, input().split())

for i in range(width + 2):
    print("#", end='')

print("")

for j in range(height):
    print("#", end='')
    str = input()
    print(str, end='')
    print("#")


for l in range(width + 2):
    print("#", end='')
