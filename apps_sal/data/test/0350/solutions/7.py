n = int(input())
ip = list(map(int, input().split()))
op = []
count = 0
for i in ip:
    if i not in op:
        count += i
        op.append(i)
    else:
        for j in range(1, i + 1):
            if i - j not in op:
                count += i - j
                op.append(i - j)
                break
            else:
                continue
print(count)
