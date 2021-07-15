from bisect import bisect


seq_l = 0
ends = [0]
template = ''
for i in range(1, 21837):
    seq_l += len(str(i))
    ends.append(ends[-1] + seq_l)
    template += str(i)

    
q = int(input())
for _ in range(q):
    k = int(input())
    i = bisect(ends, k)
    k -= ends[i - 1]
    if k == 0:
        print(str(i - 1)[-1])
    else:
        print(template[k - 1])

