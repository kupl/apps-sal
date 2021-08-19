k = int(input().strip())

num = [8, 1]
s = sum(num)
count = 0
while count < k:
    num[0] += 1
    s += 1
    #print(num, s)

    if num[0] >= 10 or s > 10:
        for i, d in enumerate(num):
            if d >= 10 or s > 10:
                num[i] = 0
                if i == len(num) - 1:  # need to add new digit
                    num.append(1)
                else:
                    num[i + 1] += 1
                s = s + 1 - d

    if s == 10:
        count += 1
        if count == k:
            print(''.join(map(str, reversed(num))))
