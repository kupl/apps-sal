import collections
N = int(input())
a = [input() for i in range(N)]
print("AC x "+str(a.count("AC")))
print("WA x "+str(a.count("WA")))
print("TLE x "+str(a.count("TLE")))
print("RE x "+str(a.count("RE")))
