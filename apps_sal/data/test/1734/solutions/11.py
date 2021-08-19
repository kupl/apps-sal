n = int(input())
mass = []
for i in range(n):
    a = input()
    mass.append(a)
# for i in range(len(mass)):
#     ans = '1' * 11
#     for j in range(len(mass[i])):
#         for k in range(j + 1, len(mass[i]) + 1):
#             cnt = 0
#             for l in range(len(mass)):
#                 if l != i:
#                     if mass[i][j:k] not in mass[l]:
#                         cnt += 1
#                     else:
#                         break
#             if cnt == n - 1:
#                 if k - j < len(ans):
#                     ans = mass[i][j:k]
#     print(ans)

a = dict()
for i in range(len(mass)):
    for j in range(len(mass[i])):
        for k in range(j + 1, len(mass[i]) + 1):
            if mass[i][j:k] in a:
                if a[mass[i][j:k]][1] != i:
                    a[mass[i][j:k]][0] += 1
                    a[mass[i][j:k]][1] = i
            else:
                a[mass[i][j:k]] = [1, i]
# print(a)
for i in range(len(mass)):
    ans = '1' * 11
    for j in range(len(mass[i])):
        for k in range(j + 1, len(mass[i]) + 1):
            if a[mass[i][j:k]][0] == 1:
                if k - j < len(ans):
                    ans = mass[i][j:k]
    print(ans)
