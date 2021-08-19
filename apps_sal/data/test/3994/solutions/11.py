# D1_B

lim = 200
arr = [0] * lim

n = int(input())

st = list(input())

for i in range(0, n):
    ln = [int(j) for j in input().split(" ")]
    a = ln[0]
    b = ln[1]
    o = [False, True][int(st[i])]
    for j in range(0, lim):
        if j < b:
            if o:
                arr[j] += 1
            continue
        if (j - b) % a == 0:
            o = not o
        if o:
            arr[j] += 1

print(max(arr))
