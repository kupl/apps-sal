
n = 0
k = ""
mem = [[-1 for xx in range(66)] for yy in range(66)]


def go(ind, po):
    nonlocal n
    nonlocal k
    nonlocal mem
    if ind >= len(k):
        return 0
    if mem[ind][po] != -1:
        return mem[ind][po]
    for i in range(ind, len(k)):
        cur = int((k[ind:i + 1])[::-1])
        if (cur >= n):
            break
        if (k[i] == '0' and i != ind):
            continue
        if (mem[ind][po] == -1):
            if(go(i + 1, po + 1) != -1):
                mem[ind][po] = cur * pow(n, po) + go(i + 1, po + 1)
        else:
            if(go(i + 1, po + 1) != -1):
                mem[ind][po] = min(mem[ind][po], cur * pow(n, po) + go(i + 1, po + 1))
    return mem[ind][po]


n = int(input())
k = input()
k = k[::-1]

print(go(0, 0))
