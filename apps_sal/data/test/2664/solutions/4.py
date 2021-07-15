print("1")
print("3 1 2 2")
print("3 3 4 4")
import sys 
d = {1:1,
     2:2,
     -1:3,
     -2:4,
     0:5
     }
sys.stdout.flush()
v = eval(input())
print("2")
print(d[v])
