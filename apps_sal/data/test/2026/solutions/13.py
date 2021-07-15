N = int(input())
s = input()
se = set()
count = 1
for i in s:
    if not i in se:
        if len(se)==2:
            count+=1
            se = {i}
        elif len(se)==0:
            se.add(i)
        else:
            if i == 'L' and 'R' in se:
                count+=1
                se = {i}
            elif i == 'R' and 'L' in se:
                count+=1
                se = {i}
            elif i == 'U' and 'D' in se:
                count+=1
                se = {i}
            elif i == 'D' and 'U' in se:
                count+=1
                se = {i}
            else:
                se.add(i)
print(count)

