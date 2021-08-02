
def f(x):
    return x[1]


L = [int(s) for s in input().split()]
n, m = L[0], L[1]
Result = [[] for i in range(m)]

for i in range(n):
    Name = [s for s in input().split()]
    region = int(Name[1]) - 1
    Result[region].append([Name[0], int(Name[2])])
for i in range(m):
    R = []
    X = sorted(Result[i], key=f)[::-1]
    R.append(X[0][0])
    R.append(X[1][0])
    if len(X) > 2 and X[2][1] == X[1][1]:
        print("?")

    else:
        print(" ".join(R))
