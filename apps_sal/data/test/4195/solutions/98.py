lst = input().split()
D = int(lst[0])
N = int(lst[1])
if N == 100:
    N += 1
print(100 ** D * N)
