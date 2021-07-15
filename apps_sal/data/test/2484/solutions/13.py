N = int(input())
ARR = list(map(int,input().split()))
def calculate(n,arr):
    right = 0
    sum = arr[0]
    result = 0

    for left in range(0,n):
        while (right + 1 < n) and ( (sum + arr[right+1]) == (sum ^ arr[right+1]) ):
            right = right + 1
            sum = sum + arr[right]

        result = result + right - left + 1
        sum = sum - arr[left]

    print(result)

calculate(N,ARR)
