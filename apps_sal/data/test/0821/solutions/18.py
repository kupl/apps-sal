from sys import stdin, stdout

s, v1,v2,t1,t2 = map(int, stdin.readline().rstrip().split())

rez1 = s * v1 + 2*t1
rez2 = s * v2 + 2*t2

if rez1 < rez2:
    print("First")
elif rez1 > rez2:
    print("Second")
else:
    print("Friendship")
