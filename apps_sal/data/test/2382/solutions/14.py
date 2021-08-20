N = int(input())
A = sorted((int(x) for x in input().split()))
parent = [A[-1]]
rest = A[:-1]
bl = True
for _ in range(N):
    next_parent = []
    next_rest = []
    for p in parent[::-1]:
        while rest:
            x = rest.pop()
            if x < p:
                next_parent.append(x)
                break
            else:
                next_rest.append(x)
                continue
    parent += next_parent
    parent.sort()
    rest = rest + next_rest[::-1]
bl = len(parent) == 2 ** N
answer = 'Yes' if bl else 'No'
print(answer)
