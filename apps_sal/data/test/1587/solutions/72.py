N = int(input())
C = input()
red_num = str.count(C, 'R')
white_num_left = str.count(C[:red_num], 'W')
min_ope = white_num_left
print(min_ope)
