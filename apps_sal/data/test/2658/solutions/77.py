N, K = list(map(int, input().split()))
A = list([int(x)-1 for x in input().split()])

cnts = [None] * N

pos = 0
cnt = 0

while cnt < K:
    if cnts[pos] != None:
        loop_size = cnt - cnts[pos]
        cnt += ((K-cnt-1) // loop_size) * loop_size
        cnts = [None] * N
    cnts[pos] = cnt
    pos = A[pos]
    cnt += 1

print((pos+1))


