MD = 1000000007
m = int(input())
p = list(map(int, input().split()))
q = {}
for el in p:
    if el in q:
        q[el] += 1
    else:
        q[el] = 2
sum1 = 1
sum2 = 1
for el in q:
    sum1 = sum1 * q[el]
    sum2 = sum2 * pow(el, (q[el] - 1), MD)
sum = pow(sum2, sum1 // 2, MD)
if sum1 % 2 == 1:
    for el in q:
        for i in range(q[el] // 2):
            sum = (sum * el) % MD
print(sum)
