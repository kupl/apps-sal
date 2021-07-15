n = int(input())
A = list(map(int,input().split()))

law_ans = 0
absminA = float('inf')
for a in A:
    law_ans += abs(a)
    absminA = min(absminA, abs(a))


cnt_neg = 0

for a in A:
    if a < 0:
        cnt_neg += 1

cnt_0 = A.count(0)

if cnt_neg%2 == 0:
    print(law_ans)
else:
    print((law_ans-2*absminA))


