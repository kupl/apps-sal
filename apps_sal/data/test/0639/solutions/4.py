(n, x) = list(map(int, input().split()))
ip = list(map(int, input().split()))
count = 0
for i in range(x):
    if i not in ip:
        ip.append(i)
        count += 1
    else:
        continue
if x not in ip:
    print(count)
else:
    print(count + 1)
