a = list(input())
count = 0
num = 0
while(a != []):
    if num == -1:
        num += 1
        continue
    if num == len(a) or len(a) == 1 or (num == len(a) - 1 and a[-1] == a[-2]):
        break
    if (a[num] == '0' and a[num + 1] == '1') or (a[num] == '1' and a[num + 1] == '0'):
        a.pop(num)
        a.pop(num)
        count += 2
        num -= 1
    else:
        num += 1
print(count)
