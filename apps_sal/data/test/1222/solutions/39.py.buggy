k = int(input())
# やっぱり一旦はglobalで書こ
total_ls = []


def dfs(A):
    if int(A) > 3234566667:
        return
    nonlocal total_ls
    total_ls.append(int(A))
    last = int(A[-1])
    if last == 0:
        nex = [1, 0]
    elif last == 9:
        nex = [8, 9]
    else:
        nex = [last - 1, last, last + 1]
    for n in nex:
        A += str(n)
        dfs(A)
        A = A[:-1]


for i in range(1, 10):
    dfs(str(i))
total_ls.sort()
print((total_ls[k - 1]))
