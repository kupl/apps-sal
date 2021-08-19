import sys
f = sys.stdin
#f = open("input.txt", "r")
n, k = map(int, f.readline().strip().split())
a = [int(i) for i in f.readline().strip().split()]
num = [True] * n * k
for i in a:
    num[i - 1] = False
for i in a:
    print(i, end=" ")
    cnt = 1
    for j in range(1, n * k + 1):
        if cnt < n:
            if num[j - 1]:
                num[j - 1] = False
                print(j, end=" ")
                cnt += 1
        else:
            break
    print()
