N = int(input())
prise = []
for _ in range(N):
    prise.append(input())
prise = list(set(prise))
print(len(prise))
