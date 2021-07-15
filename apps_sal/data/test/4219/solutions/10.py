N = int(input())
shougen = [[] for _ in range(N)]
for k in range(N):
    A = int(input())
    for j in range(A):
        x, y = list(map(int, input().split()))
        x -= 1
        shougen[k].append((x, y))
ans = 0
bit = 2**N-1
while bit:
    person = [-1 for _ in range(N)]
    b = bit
    count = 0
    while count < N:
        person[count] = b & 1
        b >>= 1
        count += 1
    flag = True
    for k in range(N):
        if person[k] == 1:
            for x, y in shougen[k]:
                if person[x] != y:
                    flag = False
                    break
            else:
                continue
            break
    if flag:
        ans = max(ans, sum(person))
    bit -= 1
print(ans)


