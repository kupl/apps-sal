import sys
read=lambda:sys.stdin.readline().rstrip()
readi=lambda:int(sys.stdin.readline())
writeln=lambda x:sys.stdout.write(str(x)+"\n")
write=lambda x:sys.stdout.write(x)
a,b=map(int, read().split())
year = 0
while a <= b:
    a*=3;b*=2
    year += 1
writeln(year)
