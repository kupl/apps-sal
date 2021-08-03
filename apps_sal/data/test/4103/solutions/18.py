n, b, a = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr1 = [b]
val = b
for i in range(1, n):
    if(arr[i] == 1):
        val -= 1
    arr1.append(val)
val = b
arr2 = [a - 1]
val2 = a - 1
ans = -1
for i in range(1, n):
    if(arr[i] == 1):
        if(val > 0):
            if(val2 == a):
                val2 -= 1
            else:
                val -= 1
                val2 = min(val2 + 1, a)
        else:
            if(val2 == 0):
                ans = i
                break
            else:
                val2 -= 1

    else:
        if(val2 == 0):
            if(val > 0):
                val -= 1
            else:
                ans = i
                break
        else:
            val2 -= 1
if(ans == -1):
    print(n)
else:
    print(ans)
