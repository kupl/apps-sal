# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
from sys import stdin, stdout


#N = int(input())
#s = input()
N, X, Y = [int(x) for x in stdin.readline().split()]

arr = [int(x) for x in stdin.readline().split()]

for i in range(N):
    left = max(0, i - X)
    right = min(N - 1, i + Y)
    # print(left,right)
    flag = 0
    for j in range(left, right + 1):
        if arr[j] <= arr[i] and i != j:
            flag = 1
            break

    if flag == 0:
        print(i + 1)
        quit()
