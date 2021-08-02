import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
def lis(): return [int(i) for i in input().split()]
def value(): return int(input())


n = value()
a = input().strip('\n')
l1, l2 = a[:(n // 2)].count('?'), a[(n // 2):].count('?')
s1 = s2 = 0
for i in range(len(a)):
    if i < n // 2:
        s1 += int(a[i]) if a[i] != '?' else 0
    else:
        s2 += int(a[i]) if a[i] != '?' else 0
no = 1
for i in range(l1):
    if s1 > s2:
        if no:
            s1 += 9
        else:
            s1 += 0
    else:
        if no:
            s1 += 0
        else:
            s1 += 9
    no = 1 - no
for i in range(l2):
    if s1 > s2:
        if no:
            s2 += 0
        else:
            s2 += 9
    else:
        if no:
            s2 += 9
        else:
            s2 += 0
    no = 1 - no
if s1 != s2:
    print('Monocarp')
else:
    print('Bicarp')
