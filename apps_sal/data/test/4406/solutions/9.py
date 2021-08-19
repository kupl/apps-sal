(n, k) = map(int, input().split())
l = [int(i) for i in input().split()]
curr = []
for i in l:
    if i in curr:
        pass
    elif len(curr) == k:
        curr.pop()
        curr.insert(0, i)
    else:
        curr.insert(0, i)
print(len(curr))
print(*curr)
