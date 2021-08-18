def solve(k):
    nonlocal a
    last_pos = 0
    while k > 0 and last_pos != len(a):
        maxInd = 0
        if k < len(a) - last_pos:
            maxDig = max(a[last_pos: last_pos + k + 1])
            for i in range(last_pos, last_pos + k + 1):
                if a[i] == maxDig:
                    maxInd = i
                    break
        else:
            maxDig = max(a[last_pos:])
            for i in range(last_pos, len(a)):
                if a[i] == maxDig:
                    maxInd = i
                    break
        if maxInd > last_pos:
            a.insert(last_pos, a[maxInd])
            temp = a.pop(maxInd + 1)
            k -= (maxInd - last_pos)
        last_pos += 1


a, k = input().split()
k = int(k)
a = list(map(int, [i for i in a]))
solve(k)
print(''.join(map(str, a)))
