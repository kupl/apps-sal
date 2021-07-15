n, m = [int(i) for i in input().split()]
line = [int(x) for x in input().split()]

count = {i+1:0 for i in range(100)}
sum = 0

for i in line:
    p = sum + i
    t = 0
    if p > m:
        for j in range(100, 0, -1):
            if count[j] == 0:
                continue
            else:
                if p - count[j] * j > m:
                    p -= count[j] * j
                    t += count[j]
                else:
                    l = (p - m) // j
                    if p - l * j > m:
                        l += 1
                    t += l
                    break
    count[i] += 1
    sum += i
    print(t, end = " ")

