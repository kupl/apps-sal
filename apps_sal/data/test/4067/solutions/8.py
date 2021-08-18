n = int(input())
s1 = str(input())
count1 = s1.count('0')
count2 = s1.count('1')
count3 = s1.count('2')
s = []
for i in s1:
    s.append(i)
finish = n // 3
tcount1 = 0
tcount2 = 0
tcount3 = 0
for i in range(n):
    if(s[i] == '0'):
        if(tcount1 == n // 3):
            if(count2 < finish and tcount2 < finish):
                s[i] = '1'
                count2 += 1
                tcount2 += 1
                count1 -= 1
            elif(count3 < finish and tcount3 < finish):
                s[i] = '2'
                count3 += 1
                tcount3 += 1
                count1 -= 1
            else:
                tcount1 += 1
        else:
            tcount1 += 1
    elif(s[i] == '1'):
        if(count2 > n // 3):
            if(count1 < n // 3 and tcount1 < n // 3):
                s[i] = '0'
                count1 += 1
                tcount1 += 1
                count2 -= 1
            elif(tcount2 == n // 3):
                s[i] = '2'
                count3 += 1
                tcount3 += 1
                count2 -= 1
            else:
                tcount2 += 1
        else:
            tcount2 += 1
    else:
        if(count3 > n // 3):
            if(count1 < n // 3 and tcount1 < n // 3):
                s[i] = '0'
                count1 += 1
                tcount1 += 1
                count3 -= 1
            elif(count2 < n // 3 and tcount2 < n // 3):
                s[i] = '1'
                count2 += 1
                tcount2 += 1
                count3 -= 1
            else:
                tcount3 += 1
        else:
            tcount3 += 1
ans = ''
for i in s:
    ans += i
print(ans)
