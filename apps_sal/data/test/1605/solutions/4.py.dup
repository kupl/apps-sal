s = input()
odd = 0
even = 0
cntE = [0, 0]
cntO = [0, 0]
for i in range(len(s)):
    cur = 0 + int(s[i] == 'b')
    odd += 1
    if i % 2 == 0:
        odd += cntE[cur]
        even += cntO[cur]
        cntE[cur] += 1
    else:
        odd += cntO[cur]
        even += cntE[cur]
        cntO[cur] += 1
print(even, odd)
