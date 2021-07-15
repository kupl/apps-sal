#Bhargey Mehta (Sophomore)
#DA-IICT, Gandhinagar
import sys, math, queue
sys.setrecursionlimit(1000000)
#sys.stdin = open("input.txt", "r")

n = int(input())
a = list(map(int, input().split()))
inc = set()
dec = set()

for ai in a:
    if ai not in inc:
        inc.add(ai)
    elif ai not in dec:
        dec.add(ai)
    else:
        print("NO")
        return

inc = sorted(inc)
dec = sorted(dec, reverse=True)
print("YES")
print(len(inc))
print(*inc)
print(len(dec))
print(*dec)

