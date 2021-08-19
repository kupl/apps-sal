from sys import stdin as fin
# fin = open("tc172b.in", "r")

# n = int(fin.readline())
n, k = map(int, fin.readline().split())
arr = list(map(int, fin.readline().split()))
# s = fin.readline().rstrip()

if k >= 3:
    print(max(arr))
elif k == 1:
    print(min(arr))
else:
    print(max(arr[0], arr[-1]))
