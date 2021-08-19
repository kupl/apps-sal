N, M = list(map(int, input().split()))
B = [0] * M
for i in range(M):
    B[i] = list(map(int, input().split()))

B = sorted(B, key=lambda x: x[1])
remove = []
# print(B)
for i in range(M):
    a, b = B[i][0], B[i][1]
    if remove == []:
        remove.append(b - 1)
    elif max(remove) >= a:
        continue
    else:
        remove.append(b - 1)
    # print(remove)
print((len(remove)))
