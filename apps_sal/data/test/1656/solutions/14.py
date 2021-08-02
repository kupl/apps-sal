s = str(input())
arr1 = []
arr2 = []
countx = 0
i = 0
while(i < len(s)):
    if(s[i] == 'o'):
        arr1.append(countx)
        i += 1
    else:
        j = i
        while(j < len(s) and s[j] == 'v'):
            j += 1
        diff = j - i
        countx += (diff - 1)
        i = j
ans = 0
# print(*arr1)
for i in range(len(arr1)):
    ans += (arr1[i] * (countx - (arr1[i])))

print(ans)
