__author__ = 'asmn'

n = int(input())
a = sorted(enumerate(map(int, input().split())),key=lambda x:-x[1])

print(a[0][0]+1, a[1][1])


