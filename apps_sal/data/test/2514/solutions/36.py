n = int(input())
al = list(map(int, input().split()))
q = int(input())

sum_n = sum(al)
num = [0]*(10**5+1)
for a in al:
    num[a] += 1

for _ in range(q):
    bi, ci = list(map(int, input().split()))
    sum_n += (ci-bi)*num[bi]
    print(sum_n)
    num[ci] += num[bi]
    num[bi] = 0

