#Bhargey Mehta (Sophomore)
#DA-IICT, Gandhinagar
import sys, math, queue
sys.setrecursionlimit(1000000)
#sys.stdin = open("input.txt", "r")

ans = []

def solve(x):
    if sorted(x) == x:
        ans.append(len(x))
    else:
        solve(x[:len(x)//2])
        solve(x[len(x)//2:])

n = int(input())
a = list(map(int, input().split()))

solve(a)
print(max(ans))
