N = int(input())

S = set()

answer = []

for x in [int(x) for x in input().split()][::-1]:
    if x not in S:
        answer.append(x)
        S.add(x)

print(len(answer))
print(' '.join(str(i) for i in answer[::-1]))
