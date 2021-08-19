__author__ = 'asmn'
n = int(input())
a = list(reversed(list(map(int, input().split()))))
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(len(a) - i)
        break
else:
    print(0)
