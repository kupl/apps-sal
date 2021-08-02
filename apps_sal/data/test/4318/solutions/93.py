# coding: utf-8

num = int(input())
str = input().split()
table = [int(i) for i in str]
count = 1
maxi = table[0]
pointed = table[0]
for i in range(1, num):
    if maxi <= table[i]:
        maxi = table[i]
        count += 1
print(count)
