a = int(input())
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while a != 0:
    b[a % 10] += 1
    a //= 10

ans = 0

def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def f(n, arr):
    #print(arr)
    nonlocal ans
    if n == 10:
        sum = 0
        for i in range(10):
            sum += arr[i]
        temp = 1
        temp *= sum - arr[0]
        #print(temp)
        temp *= fact(sum - 1)
        #print(temp)
        for i in range(10):
            if arr[i] > 1:
                temp //= fact(arr[i])
        
        ans += temp
        #print(ans)
    else:
        if b[n] > 0:
            for i in range(1, b[n] + 1):
                temp = arr.copy()
                temp.append(i)
                f(n + 1, temp)
        else:
            arr.append(0)
            f(n + 1, arr)


f(0, [])
print(int(ans))
