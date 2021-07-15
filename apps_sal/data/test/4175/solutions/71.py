N = int(input())

lst = []

for i in range(N):
    W = input()
    lst.append(W)

for n in range(1, N):
    if lst[n][0] != lst[n-1][-1] or lst.count(lst[n])>=2:
        print('No')
        break
else:
    print('Yes')
