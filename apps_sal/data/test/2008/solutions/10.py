n = int(input())
people = []
for i in range(n):
    people.append(tuple(int(x) for x in input().split()))
diss = sum(n * p[1] - p[0] for p in people)
a_b = list([p[0] - p[1] for p in people])
a_b.sort(reverse=True)
diss += sum((idx + 1) * val for idx, val in enumerate(a_b))
print(diss)
