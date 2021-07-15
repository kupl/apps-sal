n = int(input())
arr = [0] + [int(i) for i in input().split(" ")]
diff = [arr[i] - arr[i-1] for i in range(1, len(arr))]
poss = []
for xlen in range(1, len(diff)+1):
    rep = diff[0:xlen]
    for startpos in range(xlen, len(diff), xlen):
        currarr = diff[startpos:min(startpos+xlen, len(diff))]
        for obj in range(len(currarr)):
            if rep[obj] != currarr[obj]:
                break
        else:
            continue
        break
    else:
        poss.append(xlen)
print(len(poss))
print(' '.join([str(i) for i in poss]))

