n = int(input())
a = input()
z = [a[0]]
s = ['R', 'B', 'G']
count = 0
for i in range(1, n):
    if a[i]!=z[-1]:
        z.append(a[i])
    else:
        for j in s:
            if i+1 < n:
                if j != a[i+1] and j != a[i]:
                    z.append(j)
                    count+=1
                    break
            else:
                if j != a[i]:
                    z.append(j)
                    count+=1
                    break
print(count)
print(''.join(z))
