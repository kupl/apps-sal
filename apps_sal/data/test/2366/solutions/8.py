import collections
def resolve():
    n = int(input())
    a = tuple(map(int,input().split()))
    A = collections.Counter(a)
    cnt_0 = 0
    for i in A.values():
        cnt_0 += int(i*(i-1)/2)
    for i in a:
        cnt_1 = A[i]-1
        print(cnt_0-cnt_1)
resolve()
