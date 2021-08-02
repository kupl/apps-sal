N = int(input())
S = list(map(int, input().split()))

S.sort()

parent = [S.pop()]
rest = S
for _ in range(N):
    n_parent = []
    n_rest = []

    for p in parent[::-1]:
        while rest:
            x = rest.pop()
            if x < p:
                n_parent.append(x)
                break
            else:
                n_rest.append(x)
    parent += n_parent
    parent.sort()
    rest = rest + n_rest[::-1]

if len(parent) == (2**N):
    print("Yes")
else:
    print('No')
