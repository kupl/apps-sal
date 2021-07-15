t = int(input())
def check(arr, n):
    hehe = [0]*n
    for i in range (n):
        j = arr[i] - 1
        if hehe[j] == 1:
            return False
        hehe[j] += 1
    return True
for i in range (t):
    n = int(input())
    arr = list(map(int,input().split()))
    initial = [-1]*n
    diff = [n]*n
    if check(arr, n):
        print(-1)
    else:
        for j in range (n):
            l = arr[j] - 1
            k = initial[l]
            initial[l] = j
            if k == -1:
                continue
            differ = j - k + 1
            if differ < diff[l]:
                diff[l] = differ
        print(min(diff))
