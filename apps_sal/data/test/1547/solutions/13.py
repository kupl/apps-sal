INP = lambda : list(map(int, input().split()))
n,m,k = INP()
instructions = {
}
A = [[0 for i in range(m)] for j in range(n)]
for i in range(k):
    inp = INP()
    key = (inp[0],inp[1])
    val = [i,inp[2]]
    instructions[key] = val

for item in sorted(list(instructions.items()), key=lambda item: item[1][0]):
    key = item[0]
    val = item[1]
    if key[0] == 1:
        A[key[1]-1] = [val[1] for i in range(m)]
    else:
        for j in range(n):
            A[j][key[1]-1] = val[1]

for row in A:
    print(" ".join(map(str,row)))

