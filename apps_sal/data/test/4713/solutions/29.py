n = int(input())
s = input()
num_list = [0]
sum = 0
for w in s:
    if w == 'I':
        sum += 1
    else:
        sum -= 1
    num_list.append(sum)
num_list.sort()
ans = num_list[-1]
print(ans)
