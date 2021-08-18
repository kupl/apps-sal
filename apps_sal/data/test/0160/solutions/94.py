N, K = map(int, input().split())
alist = list(map(int, input().split()))

sum_a = sum(alist)
alist.sort()

divisor_set = set()
for i in range(1, int(sum_a**0.5) + 1):
    if sum_a % i == 0:
        divisor_set.add(i)
        divisor_set.add(sum_a // i)
divisor_list = list(divisor_set)
divisor_list.sort()

answer = 0
for d in divisor_list:
    rlist = []
    for a in alist:
        rlist.append((a % d, (d - a % d) % d))
    rlist.sort()

    s1list, s2list = [0], [0]
    for r1, r2 in rlist:
        s1list.append(s1list[-1] + r1)
        s2list.append(s2list[-1] + r2)

    for i in range(len(rlist)):
        r1sum = s1list[i]
        r2sum = s2list[-1] - s2list[i]
        if r1sum == r2sum and r1sum <= K:
            answer = d
            break

print(answer)
