M = int(input())
if M % 2 == 0:
    ans = M // 2 * 3
else:
    ans = M // 2 * 3 + 1
print(ans)
rua = 2
while rua <= M:
    print(rua, end=' ')
    rua += 2
rua = 1
while rua <= M:
    print(rua, end=' ')
    rua += 2
rua = 2
while rua <= M:
    print(rua, end=' ')
    rua += 2
