n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
j = 0
ansarr = [0] * m
temparr = []
for i in range(n + m):
    if(arr2[i] == 1):
        temparr.append(arr1[i])
previ = -1
for i in range(n + m):
    if(arr2[i] == 1):
        j += 1
    else:
        if(j == 0):
            ansarr[j] += 1
        elif(j == m):
            ansarr[j - 1] += 1
        else:
            dist1 = temparr[j] - arr1[i]
            dist2 = abs(arr1[i] - temparr[j - 1])
            if(dist1 >= dist2):
                ansarr[j - 1] += 1
            else:
                ansarr[j] += 1
print(*ansarr)
