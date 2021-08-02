n = int(input())
flag = True
line = input()
if line[0] == line[-1]:
    bgn = line[0]
else:
    flag = False
avr = line[1]

for i in range(n - 3):
    if not (line[i + 2] == avr):
        flag = False
        break
if not flag or avr == bgn:
    print("NO")
    return

else:
    for j in range(n - 1):
        line = input()
        k = j + 1
        for t in range(n):
            if (t == k or t == n - k - 1) and not(line[t] == bgn):
                flag = False
                break
            if not (t == k or t == n - k - 1) and not (line[t] == avr):
                flag = False
                break

if flag:
    print("YES")
else:
    print("NO")
