from sys import stdin

def valid(arr1, n, arr2, m, mid):
    tmp_list = [-1] * (m+1)
    for i in range(mid):
        if(arr1[i] > 0):
            tmp_list[arr1[i]] = i;
    
    if(tmp_list[1:].count(-1) > 0):
        return False

    stud = 0
    for i in range(mid):
        if (tmp_list[arr1[i]] == i):
            if (arr2[arr1[i]-1] <= stud):
                stud -= arr2[arr1[i]-1];
            else:
                return False
        else:
            stud += 1

    return True

def binary_search(arr1, n, arr2, m):
    l, r = 1, n
    while (l <= r):
        mid = l+r >> 1
        if (valid(arr1, n, arr2, m, mid)):
            r = mid-1
        else:
            l = mid+1
    return -1 if l == n+1 else l

def main():
    n, m = list(map(int, stdin.readline().split()))
    arr1 = list(map(int, stdin.readline().split()))
    arr2 = list(map(int, stdin.readline().split()))
    print(binary_search(arr1, n, arr2, m))

main()

