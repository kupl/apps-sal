from sys import stdin, stdout

n = int(stdin.readline())

A = stdin.readline().rstrip().split()
A = [int(num) for num in A]

B = stdin.readline().rstrip().split()
B = [int(num) for num in B]

possible = True
totSwaps = 0
for i in range(1, 6):
    if (A.count(i) + B.count(i)) % 2 == 0:
        totSwaps += int((A.count(i) + B.count(i)) / 2) - min([A.count(i), B.count(i)])
    else:
        possible = False
        break

if not possible:
    print(-1)
else:
    print(int(totSwaps / 2))
