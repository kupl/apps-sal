def solve(arr1, arr2, n):
    index = -1
    for i in range(n):
        if arr1[i] != arr2[i]:
            index = i
            diff = arr2[i] - arr1[i]
            break
    if index == -1:
        print('YES')
        return
    if diff < 0:
        print('NO')
        return
    for i in range(index, n):
        if arr1[i] == arr2[i]:
            break
        curr = arr2[i] - arr1[i]
        if curr != diff:
            print('NO')
            return
        arr2[i] = arr1[i]
    for i in range(n):
        if arr1[i] != arr2[i]:
            print('NO')
            return
    print('YES')


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        solve(arr1, arr2, n)


main()
