arr = input()
N,K = [int(num) for num in arr.split(' ')]

string = input()

seq = [string]
record = {}
record[string] = 1
count = 1


while seq and count<=105:
    gen_d = seq.pop(0)
    #print(gen_d)
    for k in range(len(gen_d)):
        r = gen_d[:k] + gen_d[(k+1):]
        if r not in record:
            record[r] = 1
            seq.append(r)
            count += 1

record[''] = 1

G = []
for s in record:
    G.append([N-len(s),s])

G.sort()
#print(G)
res = 0
if len(G)<K:
    print(-1)
else:
    for i in range(K):
        res += G[i][0]
    print(res)
