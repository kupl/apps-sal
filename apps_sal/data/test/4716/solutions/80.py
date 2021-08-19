# coding: utf-8

num, choose_num = map(int, input().split())
total = 0
stick_length = input().split(" ")

str_num = [int(n) for n in stick_length]
list.sort(str_num, reverse=True)

for i in range(choose_num):
    total += str_num[i]

print(total)
