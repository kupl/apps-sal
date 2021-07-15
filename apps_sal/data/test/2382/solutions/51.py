n = int(input())
s = list(map(int, input().split()))
rest = sorted(s)
parent = [rest.pop()]

for _ in range(n):
    next_parent = []
    next_rest = []
    for i in parent[::-1]:
        while rest:
            x = rest.pop()
            if x < i:
                next_parent.append(x)
                break
            else:
                next_rest.append(x)
                continue
    parent += next_parent
    parent.sort()
    rest += next_rest
    rest.sort()

if len(parent) == 2**n:
    print('Yes')
else:
    print('No')

