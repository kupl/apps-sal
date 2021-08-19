def calc(a, b, n):
    if b <= a:
        return n - a + b
    else:
        return b - a


inp = input().split()
n = int(inp[0])
m = int(inp[1])
seq = []
inp = input().split()
for val in inp:
    seq.append(int(val))
indices = {}
flag = 0
for i in range(len(seq) - 1):
    hop = calc(seq[i], seq[i + 1], n)
    if seq[i] in indices and indices[seq[i]] != hop:
        print('-1')
        flag = 1
        break
    indices[seq[i]] = hop
l = []
for i in range(n + 1):
    l.append(1)
flag2 = 0
if flag == 0:
    for i in range(1, n + 1):
        try:
            val = indices[i]
        except:
            continue
        if l[val] == 1:
            l[val] = 0
        else:
            print('-1')
            flag2 = 1
            break
    if flag2 == 0:
        for i in range(1, n + 1):
            try:
                print(indices[i], end=' ')
            except:
                j = 1
                while l[j] == 0:
                    j += 1
                print(j, end=' ')
                l[j] = 0
        print()
