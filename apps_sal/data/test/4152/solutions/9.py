powers = [2 ** i for i in range(31)]
n = int(input())
elems = list(map(int, input().split()))
ans = n
counter = {}
for i in elems:
    if i in list(counter.keys()):
        counter[i] += 1
    else:
        counter[i] = 1
for i in elems:
    for j in powers:
        dif = j - i
        if dif in list(counter.keys()):
            if dif == i:
                if counter[dif] > 1:
                    ans -= 1
                    break
            else:
                ans -= 1
                break
print(ans)
