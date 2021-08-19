import sys


def f(a):
    return -a[1]


fin = sys.stdin
n = int(input())
arr = list(map(int, fin.readline().split()))
arr_ind = list()
for i in range(n):
    arr_ind.append([arr[i], -i])
arr_ind.sort()
arr_ind.reverse()
ans_array = list()
for k in range(1, n + 1):
    ans = arr_ind[:k]
    ans.sort(key=f)
    ans_array.append(ans)
tests = int(input())
for test in range(tests):
    (k, pos) = map(int, input().split())
    print(ans_array[k - 1][pos - 1][0])
