(N, A, B) = list(map(int, input().split()))
al = []
for i in range(1, N + 1):
    checkno = 0
    for j in range(len(str(i))):
        str_i = str(i)
        checkno += int(str_i[j])
    if A <= checkno and checkno <= B:
        al.append(i)
print(sum(al))
