import collections
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2 == 1:
        print('Second')
    else:
        A = collections.Counter(a)
        count = list(A.values())
        f = 0
        for j in range(len(count)):
            if count[j] % 2 == 1:
                f = 1
                break
        if f == 1:
            print('First')
        else:
            print('Second')
