lst = input().split()

x = int(lst[0])
y = int(lst[1])

A = [1, 3, 5, 7, 8, 10, 12]
B = [4, 6, 9, 11]
C = [2]


def judge(L):
    if (x in L) and (y in L):
        return True
    else:
        return False


if judge(A) or judge(B) or judge(C):
    print('Yes')
else:
    print('No')
