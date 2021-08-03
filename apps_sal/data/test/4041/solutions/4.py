s = str(input())
t = str(input())
i = 0
j = 0
arr1 = []
while(i < len(s)):
    if(s[i] == t[j]):
        arr1.append(i + 1)
        j += 1
    i += 1
    if(j == len(t)):
        break

i = len(s) - 1
j = len(t) - 1
arr2 = [0] * len(t)
while(i >= 0):
    if(s[i] == t[j]):
        arr2[j] = i + 1
        j -= 1
    i -= 1
    if(j == -1):
        break

ans = max(arr2[0] - 1, len(s) - arr1[-1])

for i in range(len(t) - 1):
    ans = max(ans, arr2[i + 1] - arr1[i] - 1)

print(ans)
