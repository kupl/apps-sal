n = int(input())
shit = [0 for i in range(n + 1)]
line = input().split()
for i in range(n):
    claw = int(line[i])
    shit[i] -= 1
    pre = i - claw
    if pre < 0:
        pre = 0
    shit[pre] += 1
    continue
ans = n
tmp = 0
for i in range(n):
    tmp += shit[i]
    if tmp > 0:
        ans -= 1
    continue
print(ans)
