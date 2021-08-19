lst = input().split()
N = int(lst[0])
K = int(lst[1])
if N < K or N % K != 0:
    print(1)
else:
    print(0)
