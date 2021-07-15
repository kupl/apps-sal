# coding: utf-8
# Your code here!

n = int(input())
D = []
for i in range(n) : 
    D.append(int(input()))
D = set(D)

print(len(D))
