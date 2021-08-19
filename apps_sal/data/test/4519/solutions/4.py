import sys
input = sys.stdin.readline
q = int(input())
for testcases in range(q):
    (n, k) = list(map(int, input().split()))
    S = input().strip()
    count = 0
    LIST = [0]
    for s in S:
        if s == '1':
            count += 1
        else:
            LIST.append(count)
    ind = 1
    while ind < len(LIST) and k > 0:
        if LIST[ind] <= k:
            k -= LIST[ind]
            LIST[ind] = 0
        else:
            LIST[ind] -= k
            k = 0
        ind += 1
    ones = 0
    ANS = []
    for i in range(1, len(LIST)):
        ANS += [1] * (LIST[i] - LIST[i - 1])
        ANS.append(0)
    ANS += [1] * (count - LIST[-1])
    print(''.join(map(str, ANS)))
