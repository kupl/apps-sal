import sys

got = list(map(int, input().split()))
boys = got[0]
girls = got[1]
sys.stdout.write(str(boys + girls -1) + "\n")
for i in range(1, girls+1):
    sys.stdout.write("1 " + str(i) + "\n")
for i in range(2, boys + 1):
    sys.stdout.write(str(i) + " 1\n")

