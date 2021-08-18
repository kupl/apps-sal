n, x = map(int, input().split())
l = list(map(int, input().split()))
bound = []
for i in range(n + 1):
    if i == 0:
        bound += [0]
    else:
        bound += [bound[i - 1] + l[i - 1]]
    if bound[i] > x:
        print(len(bound) - 1)
        return
print(len(bound))
