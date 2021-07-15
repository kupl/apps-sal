from sys import stdin, stdout

n = int(stdin.readline().rstrip())
s = list(map(int,stdin.readline().rstrip().split()))
s = [i%2 for i in s]

if sum(s)==0:
    print('Second')
else:
    print('First')

