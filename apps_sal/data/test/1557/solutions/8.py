(h1, a1, c1) = list(map(int, input().strip().split()))
(h2, a2) = list(map(int, input().strip().split()))
answer = []
count = 0
while h2 > 0:
    if a1 >= h2:
        answer.append('STRIKE')
        h2 -= a1
    elif a2 >= h1:
        answer.append('HEAL')
        h1 += c1
        h1 -= a2
    else:
        answer.append('STRIKE')
        h2 -= a1
        h1 -= a2
    count += 1
print(count)
for i in answer:
    print(i)
