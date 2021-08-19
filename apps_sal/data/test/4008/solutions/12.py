def find(forb, i):
    for x in range(len(forb)):
        if i not in forb[x]:
            return x
    return -1


def new_print(arr):
    for i in arr:
        print(i, end=' ')
    print()


(n, k) = input().split()
n = int(n)
k = int(k)
arr = input().split()
map(int, arr)
ans = []
empty = set()
forb = []
for i in range(k):
    forb.append(set())
    empty.add(i)
for i in arr:
    if len(empty) != 0:
        l = empty.pop()
        ans.append(l + 1)
        forb[l].add(i)
    else:
        x = find(forb, i)
        if x == -1:
            ans = -1
            break
        forb[x].add(i)
        ans.append(x + 1)
if ans == -1:
    print('NO')
elif len(empty) != 0:
    print('NO')
else:
    print('YES')
    new_print(ans)
