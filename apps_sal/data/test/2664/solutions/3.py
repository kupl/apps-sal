import sys
print("1")
print("4 1 2 3 3")
print("4 1 4 5 5")
sys.stdout.flush()
d = {0:1,
     1:2,
     2:3,
     -1:4,
     -2:5
     }
v = eval(input())
print("2")
sys.stdout.flush()
print(d[v])
