def osilate(seq):
    flag = 1
    acc = 0
    ans = 0
    #while loop O(n)
    for i in range(len(seq)):
        a = seq[i]
        acc += a
        flag = i%2

        if flag == 0:
            if acc <= 0:
                ans += 1-acc
                acc = 1
        if flag == 1:
            if acc >= 0:
                ans += 1+acc
                acc = -1
        #print(seq, acc, acc)
        flag = flag * (-1)
    return ans

n = int(input()) #(1)
seq = [int(i) for i in input().split()] #O(N)

seq_rev = [-i for i in seq]  # O(N)
print((min(osilate(seq),osilate(seq_rev)))) #O(2N)

