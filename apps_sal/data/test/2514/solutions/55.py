n = int(input())
al = list(map(int, input().split()))
al_sum = sum(al)
q = int(input())
num = [0] * 100001
for a in al:
    num[a] += 1
for _ in range(q):
    (bi, ci) = map(int, input().split())
    al_sum += num[bi] * (ci - bi)
    num[ci] += num[bi]
    num[bi] = 0
    print(al_sum)
