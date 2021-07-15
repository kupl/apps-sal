#Bhargey Mehta (Sophomore)
#DA-IICT, Gandhinagar
import sys, math, queue, bisect
#sys.stdin = open("input.txt", "r")
MOD = 10**9+7
sys.setrecursionlimit(1000000)

def get(x):
    return sum(list(map(int, str(x))))

a = int(input())
while True:
    if get(a) % 4 == 0:
        print(a)
        return
    a += 1

