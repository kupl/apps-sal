k = int(input())
possums = {}
have_ans = False
for i in range(k):
    if have_ans:
        break

    n = input()
    seq = list(map(int, input().split(' ')))
    s = sum(seq)
    for i_in_seq, n in enumerate(seq):
        v = s - n
        if v in possums and i != possums[v][0]:
            have_ans = True
            print('YES')
            print(i + 1, i_in_seq + 1)
            print(possums[v][0] + 1, possums[v][1] + 1)
            break
        else:
            possums[v] = (i, i_in_seq)

if not have_ans:
    print('NO')
