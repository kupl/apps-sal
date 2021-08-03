i = int(input())
ctc = [0] + list(map(int, input().split()))
nm = 1
ptor = {0: 1}
for i in range(1, len(ctc)):
    if ctc[i] in list(ptor.keys()):
        ptor[i] = ptor[ctc[i]]
        del(ptor[ctc[i]])
    else:
        nm += 1
        ptor[i] = nm
print(nm)
