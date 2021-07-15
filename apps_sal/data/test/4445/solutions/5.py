n = int(input())
A = list(map(int, input().split()))
q1 = []
q2 = []
for i in A:
    if i % 2:
        q1.append(i)
    else:
        q2.append(i)
if abs(len(q1) - len(q2)) <= 1:
    print(0)
    return
if len(q1) < len(q2):
    q2.sort()
    print(sum(q2[:len(q2) - len(q1) - 1]))
else:
    q1.sort()
    print(sum(q1[:len(q1) - len(q2) - 1]))
