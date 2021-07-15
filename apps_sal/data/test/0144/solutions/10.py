n = int(input())
s = input()
arr = []
sum = 0
for i in s:
    arr.append(int(i))
    sum += (int(i))
ok = False
if (sum > 0):
    for i in range(2, sum + 1):
        if (sum % i == 0):
            sums = 0
            ok = True
            for j in range(n):
                sums += arr[j]
                if (sums == sum / i):
                    sums = 0
                elif (sums > sum / i):
                    ok = False
                    break
        if ok:
            break
else:
    ok = True
if ok:
    print("YES")
else:
    print("NO")
