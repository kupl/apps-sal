inp = input().strip().split()
inp = [int(i) for i in inp]

p = inp[0]
n = inp[1]

hashDict = {}
conflict = False
insertion = 0
for i in range(n):
    num = int(input().strip())
    num = num % p
    if num in hashDict:
        if conflict:
            continue
        conflict = True
        insertion = i

    else:
        hashDict[num] = True

if conflict:
    print(insertion + 1)
else:
    print("-1")
