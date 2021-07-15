N = int(input())
guidebook = []
for i in range(N):
    S, P = input().split()
    P = int(P)
    guidebook.append([S,P])

new_guidebook = sorted(guidebook, key=lambda x: (x[0],-x[1]))

for i in new_guidebook:
    print((guidebook.index(i)+1))

