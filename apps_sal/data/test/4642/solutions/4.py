def find(n,x,y,diff):
    arr = [x]
    while arr[-1] < y:
        arr.append(arr[-1]+diff)

    if arr[-1] != y:
        return False

    if len(arr) > n:
        return False

    min_val = arr[0]
    while len(arr) != n:
        if min_val-diff > 0:
            arr.append(min_val-diff)
            min_val -= diff
        else:
            break

    arr.sort()
    while len(arr) != n:
        arr.append(arr[-1]+diff)

    return arr

def solve(n,x,y,ans):
    for diff in range(1,100):
        arr = find(n,x,y,diff)
        if arr:
            arr1 = []
            for i in arr:
                arr1.append(str(i))

            ans.append(arr1)
            return

def main():
    t = int(input())
    ans = []
    for i in range(t):
        n,x,y = list(map(int,input().split()))
        solve(n,x,y,ans)

    for i in ans:
        print(' '.join(i))
        

main()

