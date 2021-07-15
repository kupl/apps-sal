import sys


#sys.stdin = open("input.txt")
#sys.stdout = open("output.txt", "w")

l = int(input())
p = int(input())
q = int(input())

first_t = l / (p + q)
print(p * first_t) 
