(N, M) = map(int, input().split())
div_point = int(N / 2)
if div_point % 2 == 0:
    div_point -= 1
re_point = div_point + int((N - div_point) / 2)
i = 0
while 1 < div_point - i * 2 and i < re_point and (i < M):
    ent1 = i + 1
    ent2 = div_point - i
    print(str(ent1) + ' ' + str(ent2))
    i += 1
for j in range(M - i):
    ent1 = re_point - j
    ent2 = re_point + j + 1
    print(str(ent1) + ' ' + str(ent2))
