import sys
input = sys.stdin.readline
for f in range(int(input())):
    n = int(input())
    delet = (n + 3) // 4
    rem = n - delet
    for i in range(rem):
        print(9, end='')
    for i in range(delet):
        print(8, end='')
    print()
