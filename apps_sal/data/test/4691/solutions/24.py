import collections as cs
c=cs.Counter([input() for i in range(int(input()))])
print(f'AC x {c["AC"]}')
print(f'WA x {c["WA"]}')
print(f'TLE x {c["TLE"]}')
print(f'RE x {c["RE"]}')
